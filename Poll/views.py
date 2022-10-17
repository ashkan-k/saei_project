from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, TemplateView
from ACL.mixins import PermissionMixin
from Poll.filters import PollFilters
from Poll.forms import PollForm
from Poll.models import Poll
from django.conf import settings
from django.contrib import messages

""" Poll """


class PollListView(PermissionMixin, ListView):
    permissions = ['poll_list']
    model = Poll
    context_object_name = 'polls'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'polls/admin/polls/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return PollFilters(data=self.request.GET, queryset=queryset).qs


class PollCreateView(PermissionMixin, CreateView):
    permissions = ['poll_create']
    template_name = "polls/admin/polls/form.html"
    model = Poll
    form_class = PollForm
    success_url = reverse_lazy("polls-list")


class PollUpdateView(PermissionMixin, UpdateView):
    permissions = ['poll_edit']
    template_name = "polls/admin/polls/form.html"
    model = Poll
    form_class = PollForm
    success_url = reverse_lazy("polls-list")


class PollDeleteView(PermissionMixin, DeleteView):
    permissions = ['poll_delete']
    model = Poll
    template_name = 'polls/admin/polls/list.html'
    success_url = reverse_lazy("polls-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp