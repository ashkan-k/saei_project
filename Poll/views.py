from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, TemplateView
from ACL.mixins import PermissionMixin, VerifiedUserMixin
from Poll.filters import PollFilters, UserPollFilters
from Poll.forms import PollForm, UserPollEditForm, UserPollCreateForm, UserPollDetailForm
from Poll.models import Poll, UserPoll
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
        if not self.request.user.is_staff:
            queryset = queryset.filter(
                class_item__users__in=self.request.user.classes.all(),
                is_active=True
            )
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


""" UserPoll """

class UserPollListView(VerifiedUserMixin, ListView):
    model = UserPoll
    context_object_name = 'user_polls'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'polls/admin/user_polls/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return UserPollFilters(data=self.request.GET, queryset=queryset).qs


class UserPollCreateView(VerifiedUserMixin, CreateView):
    template_name = "polls/admin/user_polls/form.html"
    model = UserPoll
    form_class = UserPollCreateForm
    success_url = reverse_lazy("user-polls-list")

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['user'] = request.user
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'نظرسنجی شما موفقیت ثبت شد.')
        return super().form_valid(form)



class UserPollUpdateView(VerifiedUserMixin, UpdateView):
    template_name = "polls/admin/user_polls/form.html"
    model = UserPoll
    form_class = UserPollEditForm
    success_url = reverse_lazy("user-polls-list")

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset


class UserPollDeleteView(VerifiedUserMixin, DeleteView):
    model = UserPoll
    template_name = 'polls/admin/user_polls/list.html'
    success_url = reverse_lazy("user-polls-list")

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class UserPollDetailView(PermissionMixin, UpdateView):
    permissions = ['poll_detail']
    template_name = "polls/admin/user_polls/detail.html"
    model = UserPoll
    form_class = UserPollDetailForm