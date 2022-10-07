from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/courses/', CoursesListView.as_view(), name='courses-list'),
    path('dashboard/courses/create/', CoursesCreateView.as_view(), name='courses-create'),
    path('dashboard/courses/update/<int:pk>/', CoursesUpdateView.as_view(), name='courses-update'),
    path('dashboard/courses/delete/<int:pk>/', CoursesDeleteView.as_view(), name='courses-delete'),

    path('dashboard/course/users/', CourseUsersListView.as_view(), name='course-users-list'),
    path('dashboard/course/users/create/', CourseUsersCreateView.as_view(), name='course-users-create'),
    path('dashboard/course/users/update/<int:pk>/', CourseUsersUpdateView.as_view(), name='course-users-update'),
    path('dashboard/course/users/delete/<int:pk>/', CourseUsersDeleteView.as_view(), name='course-users-delete'),
]

front_urls = [
    path('courses', Courses.as_view(), name='courses'),
    # path('teacher/register/', CourseRegisterView.as_view(), name='teacher-register'),
    # path('teacher/profile/', CourseProfileInfoView.as_view(), name='teacher-profile'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls
