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
