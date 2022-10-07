from ast import Pass
from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from django.urls import reverse_lazy
from ACL.mixins import SuperUserRequiredMixin, PermissionMixin
from .filters import PaymentTransactionFilters
from .models import *
from django.conf import settings
from django.contrib import messages


class PaymentTransactionListView(PermissionMixin, ListView):
    permissions = ['payments_list']
    model = PaymentTransaction
    context_object_name = 'gateways'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'gateway/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.user.is_staff:
            queryset = queryset.filter(user=self.user)
        return PaymentTransactionFilters(data=self.request.GET, queryset=queryset).qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in STATUS_CHOICES]
        context['item_type_filter_items'] = [{"name": i[1], "id": i[0]} for i in PAYMENT_ITEM_TYPES.CHOICES]
        return context
