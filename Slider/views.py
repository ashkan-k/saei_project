# from Subscription.models import Type
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
from .filters import SliderFilters
from .forms import *
from .models import Slider
from django.conf import settings
from django.contrib import messages


class SlidersListView(PermissionMixin, ListView):
    permissions = ['slider_list']
    model = Slider
    context_object_name = 'sliders'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'sliders/admin/sliders/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return SliderFilters(data=self.request.GET, queryset=queryset).qs


class SlidersCreateView(PermissionMixin, CreateView):
    permissions = ['slider_create']
    template_name = "sliders/admin/sliders/form.html"
    model = Slider
    form_class = SliderForm
    success_url = reverse_lazy("sliders-list")


class SlidersUpdateView(PermissionMixin, UpdateView):
    permissions = ['slider_edit']
    template_name = "sliders/admin/sliders/form.html"
    model = Slider
    form_class = SliderForm
    success_url = reverse_lazy("sliders-list")


class SlidersDeleteView(PermissionMixin, DeleteView):
    permissions = ['slider_delete']
    model = Slider
    template_name = 'sliders/admin/sliders/list.html'
    success_url = reverse_lazy("sliders-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
