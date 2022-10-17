from rest_framework import serializers

from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from ..models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def save(self, **kwargs):
        instance = super().save(**kwargs)

        if instance.user and hasattr(instance.user, 'phone'):
            if instance.is_approved:
                sms_text = SMS_TEXTS['teacher_approved'].format(instance.user.full_name)
                send_sms(instance.user.phone, sms_text)
            else:
                sms_text = SMS_TEXTS['teacher_reject'].format(instance.user.full_name)
                send_sms(instance.user.phone, sms_text)

        return instance

