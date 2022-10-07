import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages


class FilterInstallmentsQuerysetMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.user.is_staff:
            if self.user.role_code == 'teacher':
                queryset = queryset.filter(
                    installment__class_item_id__in=self.request.user.teacher_profile.classes.values_list('id',
                                                                                                         flat=True))
            else:
                queryset = queryset.filter(
                    installment__class_item_id__in=self.request.user.classes.values_list('class_item', flat=True))
        return queryset