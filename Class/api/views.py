import jdatetime
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ACL.rest_mixin import RestPermissionMixin
from Class.api.serializers import *
from Class.models import Class
from rest_framework.decorators import action

from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS


class ClassViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['class_list', 'class_create', 'class_edit', 'class_delete', 'class_change_status']
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUserViewSet(viewsets.ModelViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['class_user_list', 'class_user_create', 'class_user_edit', 'class_user_delete',
                   'class_user_change_status']
    queryset = ClassUser.objects.all()
    serializer_class = ClassUserSerializer


class ClassAttendanceViewSet(viewsets.GenericViewSet):
    permission_classes = [RestPermissionMixin]
    permissions = ['class_user_list', 'class_user_create', 'class_user_edit', 'class_user_delete',
                   'class_user_change_status']
    serializer_class = ClassUserAttendanceSerializer
    queryset = ClassAttendance.objects.all()

    def get_serializer_obj(self, obj=None):
        serializer = self.serializer_class(data=self.request.data)
        if obj:
            serializer.instance = obj
        serializer.is_valid(True)
        return serializer

    def send_absent_users_sms(self, users_data, instance, date):
        absent_user_phones_list = [item.user.phone for item in list(filter(lambda x: x.status == 'absent', users_data))]
        for phone in absent_user_phones_list:
            sms_text = SMS_TEXTS['absent_message'].format(str(date), instance)
            send_sms(phone, sms_text)

    @action(
        detail=False,
        methods=['post'],
        url_path='create',
    )
    def users_attendance_create(self, request):
        serializer = self.get_serializer_obj()
        users_data = serializer.validated_data.pop('data')
        instance = serializer.save()

        # create ClassAttendance obj and sync users of class to it(ClassUserAttendance)
        users_data = [
            ClassUserAttendance(user_id=item['user'], status=item['status'], desc=item['desc'], class_attendance_id=instance.id)
            for item in users_data
        ]
        ClassUserAttendance.objects.bulk_create(users_data)

        # Send absent users sms
        self.send_absent_users_sms(users_data, instance, serializer.validated_data.get('date'))
        return Response({'status': 'ok'})

    @action(
        detail=True,
        methods=['post'],
        url_path='edit',
    )
    def users_attendance_edit(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer_obj(instance)

        users_data = serializer.validated_data.pop('data')
        serializer.save()
        # save ClassAttendance obj and sync users of class to it(ClassUserAttendance)
        users_data = [
            ClassUserAttendance(pk=item['id'], user_id=item['user'], status=item['status'],
                                desc=item['desc'], class_attendance_id=pk)
            for item in users_data
        ]

        ClassUserAttendance.objects.bulk_update(users_data, ['status', 'desc'])

        # Send absent users sms
        self.send_absent_users_sms(users_data, instance, serializer.validated_data.get('date'))
        return Response({'status': 'ok'})
