from rest_framework import serializers
from ..models import *
from django_jalali.serializers.serializerfield import JDateField


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class ClassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassUser
        fields = "__all__"


class ClassUserAttendanceSerializer(serializers.ModelSerializer):
    data = serializers.ListField(child=serializers.DictField())
    date = JDateField()

    class Meta:
        model = ClassAttendance
        fields = "__all__"
