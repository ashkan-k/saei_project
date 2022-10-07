from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from ACL.mixins import PermissionMixin
from .filters import SettingFilters
from .models import *
from .forms import *


class SettingsList(PermissionMixin, ListView):
    permissions = ['setting_delete']
    model = Setting
    context_object_name = 'settings'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'settings/admin/settings/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return SettingFilters(data=self.request.GET, queryset=queryset).qs


class SettingsCreate(PermissionMixin, CreateView):
    permissions = ['setting_delete']
    model = Setting
    form_class = SettingForm
    template_name = 'settings/admin/settings/form.html'
    success_url = reverse_lazy('settings-list')


class SettingsUpdate(PermissionMixin, UpdateView):
    permissions = ['setting_delete']
    model = Setting
    form_class = SettingForm
    template_name = 'settings/admin/settings/form.html'
    success_url = reverse_lazy('settings-list')


class SettingsDelete(PermissionMixin, DeleteView):
    permissions = ['setting_delete']
    model = Setting
    template_name = 'settings/admin/settings/form.html'
    success_url = reverse_lazy('settings-list')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
