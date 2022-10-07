from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('user', CourseUserViewSet, "course_user")
router.register('', CourseViewSet, "course")

urlpatterns = [
    path('', include(router.urls))
]
