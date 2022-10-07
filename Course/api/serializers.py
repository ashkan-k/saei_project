from rest_framework import serializers
from ..models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseUser
        fields = "__all__"
