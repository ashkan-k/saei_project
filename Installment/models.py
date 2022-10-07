from django.contrib.auth import get_user_model
from django.db import models
from django_jalali.db import models as jmodels

from Class.models import Class
from utils.models import CustomModel

User = get_user_model()

"""UserInstallment Models"""


class UserInstallment(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='installments')
    class_item = models.ForeignKey(verbose_name='کلاس', to=Class, on_delete=models.CASCADE, related_name='installments')
    payment_date = jmodels.jDateField(verbose_name='سقف تاریخ پرداخت',
                                      null=True, blank=True)
    is_complete = models.BooleanField(verbose_name='آیا کامل شده است؟', default=False)

    class Meta:
        verbose_name = 'قسط پرداختی شهریه کلاس ها'
        verbose_name_plural = 'قسط پرداختی شهریه کلاس ها'

    def __str__(self):
        return f"{self.user or '---'}-{self.class_item or '---'}"

    @property
    def get_status(self):
        return 'تکمیل شده' if self.is_complete else 'تکمیل نشده'

    @property
    def get_status_class(self):
        return 'success' if self.is_complete else 'danger'


class UserInstallmentPayments(CustomModel):
    installment = models.ForeignKey(verbose_name='قسط', to=UserInstallment, on_delete=models.CASCADE,
                                    related_name='installment_payments')
    amount = models.PositiveBigIntegerField(verbose_name='مبلغ')
    is_payment = models.BooleanField(verbose_name='آیا پرداخت شده است؟', default=False)

    class Meta:
        verbose_name = 'تقسیم قسط های شهریه ها'
        verbose_name_plural = 'تقسیم قسط های شهریه ها'

    def __str__(self):
        return f"{self.installment or '---'}-{self.amount or '---'}"

    @property
    def get_status(self):
        return 'پرداخت شده' if self.is_payment else 'پرداخت نشده'

    @property
    def get_status_class(self):
        return 'success' if self.is_payment else 'danger'