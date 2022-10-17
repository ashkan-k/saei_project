from rest_framework import serializers
from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from ..models import *


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"
