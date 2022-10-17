from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.http import Http404
import jdatetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Class.models import Class, ClassUser
from Installment.models import UserInstallmentPayments, UserInstallment
from Shop.models import Product, UserProduct
from .helpers import *
from ..helpers import PAYMENT_ITEM_TYPES, PAYMENT_GATEWAYS
from ..models import PaymentTransaction


def shop_item_type_verified(user, payment_transaction):
    UserProduct.objects.create(user=user, product_id=payment_transaction.item_id,
                               pay_amount=payment_transaction.amount, status=True)


def class_item_type_verified(user, payment_transaction):
    obj, created = ClassUser.objects.get_or_create(user=user,
                                                   class_item_id=payment_transaction.item_id)
    obj.status = 'active'
    obj.save()


def installment_item_type_verified(user, payment_transaction):
    obj, created = UserInstallmentPayments.objects.get_or_create(pk=payment_transaction.item_id)
    obj.is_payment = True
    obj.save()

    is_payed_items_count = UserInstallmentPayments.objects.filter(installment=obj.installment, is_payment=True).count()

    if is_payed_items_count == obj.installment.installment_payments.count():
        obj.installment.is_complete = True
        obj.installment.save()

        class_item, _ = ClassUser.objects.get_or_create(
            user=user, class_item=obj.installment.class_item,
            status='active'
        )


#############################################################################


@api_view(['post'])
def pay(request):
    item_type = request.data.get('item_type')
    if item_type not in ['shop', 'class', 'installment']:
        return Response('لطفا نوع آیتم درگاه را مشخص کنید!', 400)

    item_id = request.data.get('item_id')
    if item_type == 'shop':
        get_object_or_404(Product, pk=item_id)
    elif item_type == 'installment':
        get_object_or_404(UserInstallmentPayments, pk=item_id)
    else:
        get_object_or_404(Class, pk=item_id)

    total_amount = request.data.get('amount')

    if total_amount == 0:
        return Response('مبلغ پرداختی 0 است!', 400)

    request.session['products_payment_amount'] = total_amount

    payment_transaction = PaymentTransaction.objects.create(
        user=request.user, gateway=PAYMENT_GATEWAYS.ZARINPAL,
        amount=total_amount, item_type=item_type, item_id=item_id,
    )

    result = client.service.PaymentRequest(
        MERCHANT, total_amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        payment_transaction.authority = str(result.Authority)
        payment_transaction.save()
        # return Response({'link': 'https://sandbox.zarinpal.com/pg/StartPay/' + str(result.Authority)}, 200)
        return Response({'link': 'https://www.zarinpal.com/pg/StartPay/' + str(result.Authority)}, 200)
    else:
        return Response('Error code: ' + str(result.Status), 400)


@login_required(login_url='/login')
def verify(request):
    payment_transaction = get_object_or_404(
        PaymentTransaction, authority=request.GET['Authority'], status='pending')

    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(
            MERCHANT, request.GET['Authority'], payment_transaction.amount)
        if result.Status == 100:
            payment_transaction.status = 'success'
            payment_transaction.ref_id = result.RefID
            payment_transaction.save()

            ## payment verified
            if payment_transaction.item_type == 'shop':
                shop_item_type_verified(request.user, payment_transaction)
            elif payment_transaction.item_type == 'class':
                class_item_type_verified(request.user, payment_transaction)
            else:
                installment_item_type_verified(request.user, payment_transaction)

            context = {"payment_transaction": payment_transaction}
            return render(request, 'gateway/payment_success.html', context)

    return render(request, 'gateway/payment_error.html', {})
