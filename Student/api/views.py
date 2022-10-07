from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ACL.rest_mixin import RestPermissionMixin
from Student.api.serializers import *
from Student.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['student_list', 'student_create', 'student_edit', 'student_delete', 'student_change_status']
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
