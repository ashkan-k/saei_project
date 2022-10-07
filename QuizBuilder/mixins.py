import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from django.contrib.auth import get_user_model

User = get_user_model()


class FilterQuizzesQuerysetMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            if self.request.user.role_code == 'teacher' and hasattr(self.request.user, 'teacher_profile'):
                queryset = queryset.filter(
                    class_item_id__in=self.request.user.teacher_profile.classes.values_list('id', flat=True))
            else:
                queryset = queryset.filter(
                    class_item_id__in=self.request.user.classes.values_list('class_item', flat=True))
        return queryset


class FilterUserQuizzesQuerysetMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            if self.request.user.role_code == 'teacher' and hasattr(self.request.user, 'teacher_profile'):
                queryset = queryset.filter(
                    quiz__class_item_id__in=self.request.user.teacher_profile.classes.values_list('id',
                                                                                                  flat=True))
            else:
                queryset = queryset.filter(
                    user=self.request.user)
        return queryset


class CheckUerQuizExpireMixin:
    def get(self, request, *args, **kwargs):
        if not self.get_user_quiz_answer_sheet.check_expire_time():
            messages.error(self.request, 'زمان پاسخ به آزمون به پایان رسیده است!')
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.get_user_quiz_answer_sheet.check_expire_time():
            messages.error(self.request, 'زمان پاسخ به آزمون به پایان رسیده است!')
            return redirect(self.success_url)


class QuizStartedSmsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_status = self.status

    # when a quiz activated and started, send sms to quiz students and teacher and admin
    def send_quiz_started_sms(self):
        expire_date = str(self.expire_time) if self.expire_time else '---'

        # Send sms to class users
        class_users = [item.user.phone for item in self.class_item.users.all()]
        for phone in class_users:
            sms_text = SMS_TEXTS['quiz_users_start'].format(self, expire_date)
            send_sms(phone, sms_text)

        # Send sms to class teacher
        if self.class_item.teacher and hasattr(self.class_item.teacher, 'user'):
            sms_text = SMS_TEXTS['quiz_teacher_start'].format(self, expire_date)
            send_sms(self.class_item.teacher.user.phone, sms_text)

        # Send sms to website admin
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            sms_text = SMS_TEXTS['quiz_admin_start'].format(self, expire_date)
            send_sms(superuser.phone, sms_text)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.status != self.last_status and self.status == 'open':
            self.send_quiz_started_sms()
