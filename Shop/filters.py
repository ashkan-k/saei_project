import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class CategoryFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(title__icontains=value) |
            Q(slug__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs


class ProductFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    category = filters.CharFilter(method="category_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(title__icontains=value) |
            Q(desc__icontains=value) |
            Q(amount__icontains=value) |
            Q(discount_amount__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def category_filter(qs, name, value):
        qs = qs.filter(category_id__in=value.split(',')).distinct()
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs


class UserProductFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    status = filters.CharFilter(method="status_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(user__first_name__icontains=value) |
            Q(user__last_name__icontains=value) |
            Q(user__national_id__icontains=value) |
            Q(user__father_name__icontains=value) |
            Q(user__phone__icontains=value) |
            Q(product__title__icontains=value) |
            Q(product__desc__icontains=value)
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
        try:
            qs = qs.filter(status=value)
        except:
            pass
        return qs
