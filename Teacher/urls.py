from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/teachers/', TeachersListView.as_view(), name='teachers-list'),
    path('dashboard/teachers/create/', TeachersCreateView.as_view(), name='teachers-create'),
    path('dashboard/teachers/update/<int:pk>/', TeachersUpdateView.as_view(), name='teachers-update'),
    path('dashboard/teachers/delete/<int:pk>/', TeachersDeleteView.as_view(), name='teachers-delete'),
    path('dashboard/teachers/detail/<int:pk>/', TeachersDetailView.as_view(), name='teachers-detail'),

    path('dashboard/teacher-attendances/', TeacherAttendancesListView.as_view(), name='teacher-attendances-list'),
    path('dashboard/teacher-attendances/create/', TeacherAttendancesCreateView.as_view(), name='teacher-attendances-create'),
    path('dashboard/teacher-attendances/update/<int:pk>/', TeacherAttendancesUpdateView.as_view(), name='teacher-attendances-update'),
    path('dashboard/teacher-attendances/delete/<int:pk>/', TeacherAttendancesDeleteView.as_view(), name='teacher-attendances-delete'),

    path('dashboard/teacher-payments/', TeacherPaymentsListView.as_view(), name='teacher-payments-list'),
    path('dashboard/teacher-payments/create/', TeacherPaymentsCreateView.as_view(), name='teacher-payments-create'),
    path('dashboard/teacher-payments/update/<int:pk>/', TeacherPaymentsUpdateView.as_view(), name='teacher-payments-update'),
    path('dashboard/teacher-payments/delete/<int:pk>/', TeacherPaymentsDeleteView.as_view(), name='teacher-payments-delete'),
]

front_urls = [
    path('teacher/register/', TeacherRegisterView.as_view(), name='teacher-register'),
    path('teacher/profile/', TeacherProfileInfoView.as_view(), name='teacher-profile'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls
