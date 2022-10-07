from django.db.models import Q
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from ACL.mixins import SuperUserRequiredMixin, PermissionMixin
# from .filters import CourseFilters
from .filters import CourseFilters, CourseUserFilters
from .forms import *
from .helpers import COURSE_STATUS, COURSE_USER_STATUS
from .models import Course, CourseUser
from django.conf import settings
from django.contrib import messages


class CoursesListView(PermissionMixin, ListView):
    permissions = ['course_list']
    model = Course
    context_object_name = 'courses'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'courses/admin/courses/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CoursesListView, self).get_context_data()
        context['change_status_form'] = CourseChangeStatusForm()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in COURSE_STATUS.CHOICES]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.user.role_code == 'teacher':
            queryset = queryset.filter(teacher__user=self.user).distinct()
        return CourseFilters(data=self.request.GET, queryset=queryset).qs


class CoursesCreateView(PermissionMixin, CreateView):
    permissions = ['course_create']
    template_name = "courses/admin/courses/form.html"
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy("courses-list")


class CoursesUpdateView(PermissionMixin, UpdateView):
    permissions = ['course_edit']
    template_name = "courses/admin/courses/form.html"
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy("courses-list")


class CoursesDeleteView(PermissionMixin, DeleteView):
    permissions = ['course_delete']
    model = Course
    template_name = 'courses/admin/courses/list.html'
    success_url = reverse_lazy("courses-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" CourseUsers """


class CourseUsersListView(PermissionMixin, ListView):
    permissions = ['course_user_list']
    model = CourseUser
    context_object_name = 'courses'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'courses/admin/course_users/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseUsersListView, self).get_context_data()
        context['change_status_form'] = CourseUserChangeStatusForm()
        context['status_filter_items'] = [{"name": i[1], "id": i[0]} for i in COURSE_USER_STATUS.CHOICES]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        course_id = self.request.GET.get('course', None)
        if course_id and int(course_id):
            queryset = queryset.filter(course_id=course_id)
        if not self.user.is_staff:
            queryset = queryset.filter(Q(user=self.user) | Q(course__teacher__user=self.user)).distinct()
        return CourseUserFilters(data=self.request.GET, queryset=queryset).qs


class CourseUsersCreateView(PermissionMixin, CreateView):
    permissions = ['course_user_create']
    template_name = "courses/admin/course_users/form.html"
    model = CourseUser
    form_class = CourseUserForm
    success_url = reverse_lazy("course-users-list")


class CourseUsersUpdateView(PermissionMixin, UpdateView):
    permissions = ['course_user_edit']
    template_name = "courses/admin/course_users/form.html"
    model = CourseUser
    form_class = CourseUserForm
    success_url = reverse_lazy("course-users-list")


class CourseUsersDeleteView(PermissionMixin, DeleteView):
    permissions = ['course_user_delete']
    model = CourseUser
    template_name = 'courses/admin/course_users/list.html'
    success_url = reverse_lazy("course-users-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Course """


class Courses(ListView):
    model = Course
    context_object_name = 'courses'
    queryset = Course.objects.all()
    paginate_by = settings.PAGINATION_NUMBER
    # ordering = ['-created_at']
    template_name = 'courses/front/courses.html'
