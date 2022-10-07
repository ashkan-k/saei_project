import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class ChatMessageFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(sender__first_name__icontains=value) |
            Q(sender__last_name__icontains=value) |
            Q(receiver__first_name__icontains=value) |
            Q(receiver__last_name__icontains=value) |
            Q(text__icontains=value)
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
