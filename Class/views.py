import jdatetime
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView, FormView
from django.urls import reverse_lazy
from ACL.mixins import SuperUserRequiredMixin, PermissionMixin
# from .filters import ClassFilters
from .filters import ClassFilters, ClassUserFilters
from .forms import *
from .helpers import CLASS_STATUS, CLASS_USER_STATUS
from .models import Class, ClassUserAttendance, ClassAttendance
from django.conf import settings
from django.contrib import messages


class ClassesListView(PermissionMixin, ListView):
    permissions = ['class_list']
    model = Class
    context_object_name = 'classes'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'classes/admin/classes/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ClassesListView, self).get_context_data()
        context['change_status_form'] = ClassChangeStatusForm()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in CLASS_STATUS.CHOICES]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.user.role_code == 'teacher':
            queryset = queryset.filter(teacher__user=self.user).distinct()
        return ClassFilters(data=self.request.GET, queryset=queryset).qs


class ClassesCreateView(PermissionMixin, CreateView):
    permissions = ['class_create']
    template_name = "classes/admin/classes/form.html"
    model = Class
    form_class = ClassForm
    success_url = reverse_lazy("classes-list")


class ClassesUpdateView(PermissionMixin, UpdateView):
    permissions = ['class_edit']
    template_name = "classes/admin/classes/form.html"
    model = Class
    form_class = ClassForm
    success_url = reverse_lazy("classes-list")


class ClassesDeleteView(PermissionMixin, DeleteView):
    permissions = ['class_delete']
    model = Class
    template_name = 'classes/admin/classes/list.html'
    success_url = reverse_lazy("classes-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class ClassesDetailView(PermissionMixin, DetailView):
    permissions = ['class_detail']
    template_name = "classes/admin/classes/detail.html"
    model = Class

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.user.role_code == 'teacher':
            queryset = queryset.filter(teacher__user=self.user).distinct()
        if not self.user.is_staff:
            queryset = queryset.filter(status='active')
        print('aaaaaaaaaaaaaaaaaaaaaaa')
        print(queryset)
        return ClassFilters(data=self.request.GET, queryset=queryset).qs


""" ClassUsers """


class ClassUsersListView(PermissionMixin, ListView):
    permissions = ['class_user_list']
    model = ClassUser
    context_object_name = 'classes'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'classes/admin/class_users/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ClassUsersListView, self).get_context_data()
        context['change_status_form'] = ClassUserChangeStatusForm()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in CLASS_USER_STATUS.CHOICES]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        class_id = self.request.GET.get('class', None)
        if class_id and int(class_id):
            queryset = queryset.filter(class_item_id=class_id)
        if not self.user.is_staff:
            queryset = queryset.filter(Q(user=self.user) | Q(class_item__teacher__user=self.user)).distinct()
        return ClassUserFilters(data=self.request.GET, queryset=queryset).qs


class ClassUsersCreateView(PermissionMixin, CreateView):
    permissions = ['class_user_create']
    template_name = "classes/admin/class_users/form.html"
    model = ClassUser
    form_class = ClassUserForm
    success_url = reverse_lazy("class-users-list")

    def get_success_url(self):
        next = self.success_url

        if self.request.GET.get('class'):
            next += '?class=' + self.request.GET.get('class')

        return next


class ClassUsersUpdateView(PermissionMixin, UpdateView):
    permissions = ['class_user_edit']
    template_name = "classes/admin/class_users/form.html"
    model = ClassUser
    form_class = ClassUserForm
    success_url = reverse_lazy("class-users-list")

    def get_success_url(self):
        next = self.success_url

        if self.request.GET.get('class'):
            next += '?class=' + self.request.GET.get('class')

        return next


class ClassUsersDeleteView(PermissionMixin, DeleteView):
    permissions = ['class_user_delete']
    model = ClassUser
    template_name = 'classes/admin/class_users/list.html'
    success_url = reverse_lazy("class-users-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


class ClassUsersGatewayView(PermissionMixin, DetailView):
    permissions = ['class_user_detail']
    model = Class
    template_name = 'classes/admin/class_users/payment.html'
    context_object_name = 'class_detail'


"""Class Attendance"""


class ClassAttendanceDailyListView(PermissionMixin, ListView):
    permissions = ['class_attendance_list']
    template_name = "classes/admin/attendances/daily_list.html"
    model = ClassUserAttendance

    def get_queryset(self):
        today_date = jdatetime.datetime.now().date()
        queryset = ClassUserAttendance.objects.filter(
            created_at__year=today_date.year,
            created_at__month=today_date.month,
            created_at__day=today_date.day,
        )
        print(ClassUserAttendance.objects.filter(
            created_at__year='1401'
        ))
        print(today_date.year)
        print(type(today_date.year))
        print(today_date.year == 1401)

        return queryset


class ClassAttendanceView(PermissionMixin, DetailView):
    permissions = ['class_attendance_list']
    template_name = "classes/admin/attendances/list.html"
    model = Class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = ClassAttendance.objects.filter(class_item=self.object)
        return context


class ClassAttendancesCreateView(PermissionMixin, FormView):
    permissions = ['class_attendance_create']
    template_name = "classes/admin/attendances/form.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Class, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = {
            'class_object': object,
            'object_list': object.users.all(),
            'form': ClassAttendanceForm(initial={'class_item': self.kwargs.get('pk')}),
        }
        return context


class ClassAttendancesUpdateView(PermissionMixin, UpdateView):
    permissions = ['class_attendance_edit']
    template_name = "classes/admin/attendances/form.html"
    model = ClassAttendance
    form_class = ClassAttendanceForm
    success_url = reverse_lazy("class-users-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_object'] = self.object.class_item
        context['object_list'] = self.object.class_item.users.all()
        return context


class ClassAttendancesDeleteView(PermissionMixin, DeleteView):
    permissions = ['class_attendance_delete']
    model = ClassAttendance
    template_name = 'classes/admin/attendances/list.html'
    success_url = reverse_lazy("class-users-list")

    def get_success_url(self):
        next = self.success_url

        if self.request.GET.get('next'):
            next = self.request.GET.get('next')

        return next

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Front """


class Classes(ListView):
    model = Class
    context_object_name = 'classes'
    queryset = Class.objects.filter(status='active')
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'classes/front/classes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update(last_class=Class.objects.filter(status='active').last())
        return super(Classes, self).get_context_data(object_list=None, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search')
        if search:
            q = Q(title__icontains=search) | Q(desc__icontains=search) | Q(
                teacher__user__first_name__icontains=search) | Q(teacher__user__last_name__icontains=search)
            qs = qs.filter(q)

        return qs


class ClassesDetail(DetailView):
    model = Class
    slug_field = 'slug'
    queryset = Class.objects.filter(status='active')
    template_name = 'classes/front/detail.html'

