from rest_framework import serializers

from User.api.serializers import UserSerializer
from ..models import *
from django_jalali.serializers.serializerfield import JDateField


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['sender'] = UserSerializer().to_representation(instance.sender if instance.sender else None)
        rep['receiver'] = UserSerializer().to_representation(instance.receiver if instance.receiver else None)
        rep['created_at'] = instance.created_at.strftime("%H:%M %Y/%m/%d") if instance.created_at else None
        return rep
