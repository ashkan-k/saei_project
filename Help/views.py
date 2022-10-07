from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from ACL.mixins import PermissionMixin
from .filters import *
from .forms import *
from .models import Help

""" Helps """


class HelpsListView(PermissionMixin, ListView):
    permissions = ['helps_list']
    model = Help
    context_object_name = 'helps'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'help/admin/helps/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return HelpFilters(data=self.request.GET, queryset=queryset).qs


class HelpsCreateView(PermissionMixin, CreateView):
    permissions = ['helps_create']
    template_name = "help/admin/helps/form.html"
    model = Help
    form_class = HelpForm
    success_url = reverse_lazy("helps-list")


class HelpsUpdateView(PermissionMixin, UpdateView):
    permissions = ['helps_create']
    template_name = "help/admin/helps/form.html"
    model = Help
    form_class = HelpForm
    success_url = reverse_lazy("helps-list")


class HelpsDeleteView(PermissionMixin, DeleteView):
    permissions = ['helps_delete']
    model = Help
    template_name = 'help/admin/helps/list.html'
    success_url = reverse_lazy("helps-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
