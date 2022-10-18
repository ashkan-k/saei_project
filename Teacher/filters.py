import django_filters as filters
from django.db.models import Q, Value
from django.db.models.functions import Concat
from unidecode import unidecode


class TeacherFilters(filters.FilterSet):
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
            Q(user__phone__icontains=value)
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
        qs = qs.filter(is_approved=value)
        return qs


class TeacherAttendanceFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    teacher = filters.CharFilter(method="teacher_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(teacher__user__first_name__icontains=value) |
            Q(teacher__user__last_name__icontains=value) |
            Q(teacher__user__national_id__icontains=value) |
            Q(teacher__user__father_name__icontains=value) |
            Q(teacher__user__phone__icontains=value) |
            Q(desc__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def teacher_filter(qs, name, value):
        qs = qs.filter(teacher_id=value)
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs


class TeacherPaymentFilters(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")
    teacher = filters.CharFilter(method="teacher_filter")
    limit = filters.CharFilter(method="limit_filter")

    @staticmethod
    def search_filter(qs, name, value):
        qs = qs.filter(
            Q(teacher__user__first_name__icontains=value) |
            Q(teacher__user__last_name__icontains=value) |
            Q(teacher__user__national_id__icontains=value) |
            Q(teacher__user__father_name__icontains=value) |
            Q(teacher__user__phone__icontains=value) |
            Q(amount__icontains=value)
        ).distinct()
        return qs

    @staticmethod
    def teacher_filter(qs, name, value):
        qs = qs.filter(teacher_id=value)
        return qs

    @staticmethod
    def limit_filter(qs, name, value):
        try:
            qs = qs.distinct()[:int(unidecode(value))]
        except:
            pass
        return qs
