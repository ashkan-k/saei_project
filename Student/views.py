# from Subscription.models import Type
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
from .filters import StudentFilters
from .forms import *
from .models import Student
from django.conf import settings
from django.contrib import messages


class StudentRegisterView(AnonymousUserMixin, CreateView):
    template_name = "auth/register.html"
    model = User
    form_class = UserSimpleForm
    success_url = reverse_lazy("verify-code")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form = super().form_valid(form)
        Student.objects.create(user=self.object)
        return form


class StudentProfileInfoView(VerifiedUserMixin, UpdateView):
    template_name = "students/registration/form.html"
    model = User
    queryset = User.objects.filter(student_profile__isnull=False)
    form_class = StudentForm
    success_url = reverse_lazy("dashboard")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('phone', '')
        form.fields.pop('password', '')

        return form

    def get_object(self, queryset=None):
        return self.request.user


##########################################################

class StudentsListView(PermissionMixin, ListView):
    permissions = ['student_list']
    model = Student
    context_object_name = 'students'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'students/admin/students/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return StudentFilters(data=self.request.GET, queryset=queryset).qs


class StudentsCreateView(PermissionMixin, CreateView):
    permissions = ['student_create']
    template_name = "students/admin/students/form.html"
    model = User
    form_class = StudentForm
    success_url = reverse_lazy("students-list")


class StudentsUpdateView(PermissionMixin, UpdateView):
    permissions = ['student_edit']
    template_name = "students/admin/students/form.html"
    model = User
    form_class = StudentForm
    success_url = reverse_lazy("students-list")


class StudentsDetailView(PermissionMixin, DetailView):
    permissions = ['student_detail']
    template_name = "students/admin/students/profile.html"
    model = Student


class StudentsDeleteView(PermissionMixin, DeleteView):
    permissions = ['student_delete']
    model = User
    template_name = 'students/admin/students/list.html'
    success_url = reverse_lazy("students-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp
