from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ACL.rest_mixin import RestPermissionMixin
from Installment.api.serializers import *
from Installment.models import UserInstallment
from rest_framework.decorators import action
from rest_framework.decorators import action


class UserInstallmentViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['installment_list', 'installment_create', 'installment_edit', 'installment_delete',
                   'installment_detail']
    queryset = UserInstallment.objects.all()
    serializer_class = UserInstallmentSerializer

    @action(
        detail=True,
        methods=['get'],
        url_path='payment-items',
        serializer_class=UserInstallmentPaymentsSerializer
    )
    def get_payment_items_api(self, request, pk):
        installment = self.get_object()
        serializer = self.get_serializer(installment.installment_payments.all(), many=True)
        return Response(serializer.data)


class UserInstallmentPaymentsViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = [
        'installment_items_list',
        'installment_items_create',
        'installment_items_edit',
        'installment_items_delete',
        'installment_items_detail'
    ]
    queryset = UserInstallmentPayments.objects.all()
    serializer_class = UserInstallmentPaymentsSerializer
