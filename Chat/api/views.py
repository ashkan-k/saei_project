from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ACL.rest_mixin import RestPermissionMixin
from Chat.api.serializers import *
from Chat.models import ChatMessage
from rest_framework.decorators import action


class ChatMessageViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['chats_list', 'chats_create', 'chats_edit', 'chats_delete']
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            receiver = self.request.GET.get('receiver')
            if not receiver:
                raise PermissionDenied

            q = Q(sender=self.request.user, receiver=receiver) | Q(sender=receiver, receiver=self.request.user)
            qs = qs.filter(q).distinct()

        return qs.order_by('created_at')
