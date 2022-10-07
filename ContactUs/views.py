# from Subscription.models import Type
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
from .filters import SuggestionFilters, ContactUsFilters
from .forms import *
from .mixins import FilterSuggestionsQuerysetMixin
from .models import Suggestion
from django.conf import settings
from django.contrib import messages


class SuggestionListView(PermissionMixin, FilterSuggestionsQuerysetMixin, ListView):
    permissions = ['suggestion_list']
    model = Suggestion
    context_object_name = 'suggestions'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'contact_us/admin/suggestions/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return SuggestionFilters(data=self.request.GET, queryset=queryset).qs


class SuggestionCreateView(PermissionMixin, CreateView):
    permissions = ['suggestion_create']
    template_name = "contact_us/admin/suggestions/form.html"
    model = Suggestion
    form_class = SuggestionForm
    success_url = reverse_lazy("suggestions-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class SuggestionUpdateView(PermissionMixin, FilterSuggestionsQuerysetMixin, UpdateView):
    permissions = ['suggestion_edit']
    template_name = "contact_us/admin/suggestions/form.html"
    model = Suggestion
    form_class = SuggestionForm
    success_url = reverse_lazy("suggestions-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class SuggestionDeleteView(PermissionMixin, FilterSuggestionsQuerysetMixin, DeleteView):
    permissions = ['suggestion_delete']
    model = Suggestion
    template_name = 'contact_us/admin/suggestions/list.html'
    success_url = reverse_lazy("suggestions-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" ContactUs """


class ContactUsListView(PermissionMixin, ListView):
    permissions = ['contact_us_list']
    model = ContactUs
    context_object_name = 'suggestions'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'contact_us/admin/contact_us/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return ContactUsFilters(data=self.request.GET, queryset=queryset).qs


class ContactUsDeleteView(PermissionMixin, DeleteView):
    permissions = ['contact_us_delete']
    model = ContactUs
    template_name = 'contact_us/admin/contact_us/list.html'
    success_url = reverse_lazy("contact_us-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Front Side """


class ContactUsView(CreateView):
    template_name = "contact_us/front/contact_us.html"
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy("contact_us")

    def post(self, request, *args, **kwargs):
        messages.success(self.request, 'پیام تماس شما با موفقیت ثبت شد.')
        return super().post(request, *args, **kwargs)
