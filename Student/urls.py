from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/students/', StudentsListView.as_view(), name='students-list'),
    path('dashboard/students/create/', StudentsCreateView.as_view(), name='students-create'),
    path('dashboard/students/update/<int:pk>/', StudentsUpdateView.as_view(), name='students-update'),
    path('dashboard/students/delete/<int:pk>/', StudentsDeleteView.as_view(), name='students-delete'),
    path('dashboard/students/detail/<int:pk>/', StudentsDetailView.as_view(), name='students-detail'),
]

front_urls = [
    path('student/register/', StudentRegisterView.as_view(), name='student-register'),
    path('student/profile/', StudentProfileInfoView.as_view(), name='student-profile'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls
