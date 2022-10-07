from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from django.urls import reverse_lazy
from ACL.mixins import SuperUserRequiredMixin, PermissionMixin
# from .filters import ClassFilters, ClassUserFilters
# from .forms import *
from Student.models import Student
from Teacher.models import Teacher
from .filters import ChatMessageFilters
from .models import ChatMessage
from django.conf import settings
from django.contrib import messages

User = get_user_model()


class ChatMessageListView(PermissionMixin, ListView):
    permissions = ['chats_list']
    model = ChatMessage
    context_object_name = 'objects'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['created_at']
    template_name = 'chats/admin/chats/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            q = Q(sender=self.request.user) | Q(receiver=self.request.user)
            queryset = queryset.filter(q).distinct()

        return ChatMessageFilters(data=self.request.GET, queryset=queryset).qs.order_by('-created_at')


class ChatMessageRoomView(PermissionMixin, DetailView):
    permissions = ['chats_create']
    template_name = "chats/admin/chats/form.html"

    def get_queryset(self):
        if self.request.user.role_code == 'student':
            return User.objects.filter(teacher_profile__isnull=False, teacher_profile__is_approved=True)
        return User.objects.filter(student_profile__isnull=False, student_profile__is_approved=True)


class ChatMessagesDeleteView(PermissionMixin, DeleteView):
    permissions = ['chats_delete']
    model = ChatMessage
    template_name = 'chats/admin/chats/form.html'
    success_url = reverse_lazy("chats-list")

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            q = Q(sender=self.request.user) | Q(receiver=self.request.user)
            qs = qs.filter(q).distinct()

        return qs.order_by('created_at')

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
