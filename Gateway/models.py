import jdatetime

from django.db import models
from django.contrib.auth import get_user_model

from .helpers import *
from utils.models import CustomModel

User = get_user_model()


class PaymentTransaction(CustomModel):
    user = models.ForeignKey(
        to=User,
        db_index=True,
        null=True,
        on_delete=models.CASCADE,
    )

    gateway = models.CharField(
        default="",
        max_length=10,
        choices=PAYMENT_GATEWAYS.CHOICES,
    )

    amount = models.IntegerField(default=0)

    status = models.CharField(
        db_index=True,
        max_length=10,
        default="pending",
        choices=STATUS_CHOICES,
    )

    ref_id = models.CharField(max_length=255, null=True, blank=True)

    authority = models.CharField(max_length=255, null=True, blank=True)

    item_type = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name="نوع آیتم",
        choices=PAYMENT_ITEM_TYPES.CHOICES,
    )
    item_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="شناسه آیتم",
    )

    # # payment and other links to redirect
    # payment_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return "{}, {}, {}, {} ریال".format(
            self.get_status_display(),
            self.get_gateway_display(),
            self.authority,
            self.amount
        )

    class Meta:
        verbose_name = "تراکنش درگاه پرداخت"
        verbose_name_plural = "تراکنش های درگاه پرداخت"

    @property
    def status_display(self):
        return self.get_status_display()

    @property
    def get_status_class(self):
        return dict(STATUS_CASS_CHOICES).get(self.status, '')

    @property
    def get_item_type_class(self):
        return dict(PAYMENT_ITEM_TYPES_CLASS.CHOICES).get(self.item_type, '')

    @property
    def gateway_display(self):
        return self.get_gateway_display()

    @property
    def item_type_display(self):
        return dict(PAYMENT_ITEM_TYPES.CHOICES).get(self.item_type, '')

    def save(self, *args, **kwargs):
        if not self.gateway:
            self.gateway = PAYMENT_GATEWAYS.ZARINPAL
        return super().save(*args, **kwargs)
