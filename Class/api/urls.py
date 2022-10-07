from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('attendance', ClassAttendanceViewSet, "attendance_user")
router.register('user', ClassUserViewSet, "class_user")
router.register('', ClassViewSet, "class")

urlpatterns = [
    path('', include(router.urls))
]
