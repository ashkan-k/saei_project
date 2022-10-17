from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from ACL.rest_mixin import RestPermissionMixin
from Poll.api.serializers import *
from Poll.models import Poll


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['poll_list', 'poll_create', 'poll_edit', 'poll_delete', 'poll_change_status']
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
