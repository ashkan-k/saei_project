import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode

from Shop.models import Product


class PaymentTransactionFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    status = filters.CharFilter(method="status_filter")
    item_type = filters.CharFilter(method="item_type_filter")
    category = filters.CharFilter(method="category_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(user__first_name__icontains=value) |
            Q(user__last_name__icontains=value) |
            Q(user__national_id__icontains=value) |
            Q(user__father_name__icontains=value) |
            Q(user__phone__icontains=value) |
            Q(amount__icontains=value) |
            Q(ref_id__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs

    @staticmethod
    def status_filter(qs, name, value):
        qs = qs.filter(status=value)
        return qs

    @staticmethod
    def item_type_filter(qs, name, value):
        qs = qs.filter(item_type=value)
        return qs

    @staticmethod
    def category_filter(qs, name, value):
        product_ids = Product.objects.filter(category_id=value)
        qs = qs.filter(item_id__in=product_ids, item_type='shop')
        return qs
