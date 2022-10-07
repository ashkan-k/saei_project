from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ACL.rest_mixin import RestPermissionMixin
from Course.api.serializers import *
from Course.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['course_list', 'course_create', 'course_edit', 'course_delete', 'course_change_status']
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUserViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['course_user_list', 'course_user_create', 'course_user_edit', 'course_user_delete',
                   'course_user_change_status']
    queryset = CourseUser.objects.all()
    serializer_class = CourseUserSerializer
