from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from Teacher.api.serializers import *
from Teacher.models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
