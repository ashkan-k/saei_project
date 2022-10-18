# from Subscription.models import Type
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
from .filters import TeacherFilters, TeacherAttendanceFilters, TeacherPaymentFilters
from .forms import *
from .models import Teacher
from django.conf import settings
from django.contrib import messages


class TeacherRegisterView(AnonymousUserMixin, CreateView):
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
        Teacher.objects.create(user=self.object)
        return form


class TeacherProfileInfoView(VerifiedUserMixin, UpdateView):
    template_name = "teachers/registration/form.html"
    model = User
    queryset = User.objects.filter(teacher_profile__isnull=False)
    form_class = TeacherForm
    success_url = reverse_lazy("dashboard")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('phone', '')
        form.fields.pop('password', '')

        return form

    def get_object(self, queryset=None):
        return self.request.user


##########################################################

class TeachersListView(PermissionMixin, ListView):
    permissions = ['teacher_list']
    model = Teacher
    context_object_name = 'teachers'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'teachers/admin/teachers/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in (('1', 'تایید شده'), ('0', 'تایید نشده'))]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return TeacherFilters(data=self.request.GET, queryset=queryset).qs


class TeachersCreateView(PermissionMixin, CreateView):
    permissions = ['teacher_create']
    template_name = "teachers/admin/teachers/form.html"
    model = User
    form_class = TeacherForm
    success_url = reverse_lazy("teachers-list")


class TeachersUpdateView(PermissionMixin, UpdateView):
    permissions = ['teacher_edit']
    template_name = "teachers/admin/teachers/form.html"
    model = User
    form_class = TeacherForm
    success_url = reverse_lazy("teachers-list")


class TeachersDetailView(PermissionMixin, DetailView):
    permissions = ['teacher_detail']
    template_name = "teachers/admin/teachers/profile.html"
    model = Teacher


class TeachersDeleteView(PermissionMixin, DeleteView):
    permissions = ['teacher_delete']
    model = User
    template_name = 'teachers/admin/teachers/list.html'
    success_url = reverse_lazy("teachers-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


##########################################################

class TeacherAttendancesListView(PermissionMixin, ListView):
    permissions = ['teacher_list']
    model = TeacherAttendance
    context_object_name = 'teacher_attendances'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'teachers/admin/teacher_attendances/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['teacher_filter_items'] = [{"name": i.__str__(), "id": i.id} for i in Teacher.objects.all()]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return TeacherAttendanceFilters(data=self.request.GET, queryset=queryset).qs


class TeacherAttendancesCreateView(PermissionMixin, CreateView):
    permissions = ['teacher_create']
    template_name = "teachers/admin/teacher_attendances/form.html"
    model = TeacherAttendance
    form_class = TeacherAttendanceForm
    success_url = reverse_lazy("teacher-attendances-list")


class TeacherAttendancesUpdateView(PermissionMixin, UpdateView):
    permissions = ['teacher_edit']
    template_name = "teachers/admin/teacher_attendances/form.html"
    model = TeacherAttendance
    form_class = TeacherAttendanceForm
    success_url = reverse_lazy("teacher-attendances-list")


class TeacherAttendancesDeleteView(PermissionMixin, DeleteView):
    permissions = ['teacher_delete']
    model = TeacherAttendance
    template_name = 'teachers/admin/teacher_attendances/list.html'
    success_url = reverse_lazy("teacher-attendances-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


##########################################################

class TeacherPaymentsListView(PermissionMixin, ListView):
    permissions = ['teacher_list']
    model = TeacherPayment
    context_object_name = 'teacher_attendances'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'teachers/admin/teacher_payments/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['teacher_filter_items'] = [{"name": i.__str__(), "id": i.id} for i in Teacher.objects.all()]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return TeacherPaymentFilters(data=self.request.GET, queryset=queryset).qs


class TeacherPaymentsCreateView(PermissionMixin, CreateView):
    permissions = ['teacher_create']
    template_name = "teachers/admin/teacher_payments/form.html"
    model = TeacherPayment
    form_class = TeacherPaymentForm
    success_url = reverse_lazy("teacher-payments-list")


class TeacherPaymentsUpdateView(PermissionMixin, UpdateView):
    permissions = ['teacher_edit']
    template_name = "teachers/admin/teacher_payments/form.html"
    model = TeacherPayment
    form_class = TeacherPaymentForm
    success_url = reverse_lazy("teacher-payments-list")


class TeacherPaymentsDeleteView(PermissionMixin, DeleteView):
    permissions = ['teacher_delete']
    model = TeacherPayment
    template_name = 'teachers/admin/teacher_payments/list.html'
    success_url = reverse_lazy("teacher-payments-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp