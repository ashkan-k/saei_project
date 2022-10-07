from django.db.models import Sum
from rest_framework import serializers
from ..models import *
from django_jalali.serializers.serializerfield import JDateField


class UserInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInstallment
        fields = "__all__"


class UserInstallmentPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInstallmentPayments
        fields = "__all__"

    def validate(self, attrs):
        installment = attrs.get('installment')

        qs = UserInstallmentPayments.objects.filter(installment=installment)
        if self.instance:
            qs = qs.exclude(pk=self.instance.id)

        total_payments_amount = qs.aggregate(
            Sum('amount')
        )['amount__sum'] or 0

        if (total_payments_amount + attrs.get('amount')) > installment.class_item.amount:
            raise serializers.ValidationError('مجموع قیمت اقساط بیشتر از شهریه کلاس است!', code='amount')

        return attrs
