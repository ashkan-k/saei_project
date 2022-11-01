from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/classes/', ClassesListView.as_view(), name='classes-list'),
    path('dashboard/classes/my/', ClassesListView.as_view(), name='my-classes-list'),
    path('dashboard/classes/create/', ClassesCreateView.as_view(), name='classes-create'),
    path('dashboard/classes/update/<int:pk>/', ClassesUpdateView.as_view(), name='classes-update'),
    path('dashboard/classes/delete/<int:pk>/', ClassesDeleteView.as_view(), name='classes-delete'),
    path('dashboard/classes/detail/<int:pk>/', ClassesDetailView.as_view(), name='classes-detail'),

    path('dashboard/class/users/', ClassUsersListView.as_view(), name='class-users-list'),
    path('dashboard/class/users/create/', ClassUsersCreateView.as_view(), name='class-users-create'),
    path('dashboard/class/users/update/<int:pk>/', ClassUsersUpdateView.as_view(), name='class-users-update'),
    path('dashboard/class/users/delete/<int:pk>/', ClassUsersDeleteView.as_view(), name='class-users-delete'),
    path('dashboard/class/users/gateway/<int:pk>', ClassUsersGatewayView.as_view(), name='class-users-gateway'),
    path('dashboard/class/users/all/change-status/<int:pk>', ClassUsersChangeAllStatusView.as_view(), name='class-users-all-change-status'),

    path('dashboard/class/users/attendances/daily/', ClassAttendanceDailyAbsentsListView.as_view(),
         name='class-attendances-daily-list'),
    path('dashboard/class/users/attendances/<int:pk>/', ClassAttendanceView.as_view(),
         name='class-attendances-list'),
    path('dashboard/class/users/attendances/create/<int:pk>/', ClassAttendancesCreateView.as_view(),
         name='class-attendances-create'),
    path('dashboard/class/users/attendances/update/<int:pk>/', ClassAttendancesUpdateView.as_view(),
         name='class-attendances-update'),
    path('dashboard/class/users/attendances/delete/<int:pk>/', ClassAttendancesDeleteView.as_view(),
         name='class-attendances-delete'),
]

front_urls = [
    path('classes/', Classes.as_view(), name='classes'),
    path('classes/<str:slug>/', ClassesDetail.as_view(), name='class-details'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls
