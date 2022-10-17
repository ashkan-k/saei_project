import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class PollFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(class_item__title__icontains=value)
        ).distinct()
        return qs


class UserPollFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(poll__class_item__title__icontains=value) |
            Q(user__first_name__icontains=value) |
            Q(user__last_name__icontains=value) |
            Q(user__phone__icontains=value) |
            Q(user__national_id__icontains=value)
        ).distinct()
        return qs
