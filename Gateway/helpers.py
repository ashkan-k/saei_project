class PAYMENT_ITEM_TYPES:
    SHOP = "shop"
    CLASS = "class"
    INSTALLMENT = "installment"
    CHOICES = (
        (SHOP, "فروشگاه"),
        (CLASS, "شهریه کلاس"),
        (INSTALLMENT, "قسط شهریه کلاس"),
    )


class PAYMENT_ITEM_TYPES_CLASS:
    SHOP = "shop"
    CLASS = "class"
    INSTALLMENT = "installment"
    CHOICES = (
        (SHOP, "warning"),
        (CLASS, "info"),
        (INSTALLMENT, "success"),
    )


class PAYMENT_GATEWAYS:
    ZARINPAL = "zarinpal"
    CHOICES = (
        (ZARINPAL, "زرین پال"),
    )


STATUS_CHOICES = (
    ("pending", "در حال انتظار"),
    ("success", "موفقیت‌آمیز"),
    ("failed", "ناموفق"),
)

STATUS_CASS_CHOICES = (
    ("pending", "warning"),
    ("success", "success"),
    ("failed", "danger"),
)
