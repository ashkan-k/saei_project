from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from django.conf import settings
from django.contrib import messages
from ACL.mixins import SuperUserRequiredMixin, PermissionMixin
from django.urls import reverse_lazy
from .filters import *
from .forms import *
from .mixins import FilterInstallmentsQuerysetMixin

"""UserInstallment"""


class UserInstallmentListView(PermissionMixin, ListView):
    permissions = ['installment_list']
    model = UserInstallment
    context_object_name = 'installments'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'installments/admin/installments/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserInstallmentListView, self).get_context_data()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in ((1, 'تکمیل شده'), (0, 'تکمیل نشده'))]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserInstallmentFilters(data=self.request.GET, queryset=queryset).qs


class UserInstallmentCreateView(PermissionMixin, CreateView):
    permissions = ['installment_create']
    template_name = "installments/admin/installments/form.html"
    model = UserInstallment
    form_class = UserInstallmentForm
    success_url = reverse_lazy("installments-list")

    def get_success_url(self):
        return reverse_lazy("installments-update", kwargs={'pk': self.object.id})


class UserInstallmentUpdateView(PermissionMixin, UpdateView):
    permissions = ['installment_edit']
    template_name = "installments/admin/installments/form.html"
    model = UserInstallment
    form_class = UserInstallmentForm
    success_url = reverse_lazy("installments-list")


class UserInstallmentDeleteView(PermissionMixin, DeleteView):
    permissions = ['installment_delete']
    model = UserInstallment
    template_name = 'installments/admin/installments/list.html'
    success_url = reverse_lazy("installments-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


"""UserInstallmentPayments"""


class UserInstallmentPaymentsListView(PermissionMixin, FilterInstallmentsQuerysetMixin, ListView):
    permissions = ['installment_items_list']
    model = UserInstallmentPayments
    context_object_name = 'installments'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'installments/admin/installment-items/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('pk'):
            queryset = queryset.filter(installment_id=self.kwargs.get('pk'))
        return queryset


class UserInstallmentPaymentsDeleteView(PermissionMixin, DeleteView):
    permissions = ['installment_items_delete']
    model = UserInstallmentPayments
    template_name = 'installments/admin/installment-items/list.html'
    success_url = reverse_lazy("installments-items-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class UserInstallmentPaymentsDetailView(PermissionMixin, FilterInstallmentsQuerysetMixin, DetailView):
    permissions = ['installment_items_detail']
    template_name = "installments/admin/installment-items/detail.html"
    model = UserInstallmentPayments


class UserInstallmentPaymentsGatewayView(PermissionMixin, DetailView):
    permissions = ['installment_items_detail']
    model = UserInstallmentPayments
    template_name = 'installments/admin/installment-items/payment.html'
