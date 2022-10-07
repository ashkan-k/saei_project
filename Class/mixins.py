from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from django.contrib.auth import get_user_model

User = get_user_model()


class ClassStartedSmsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_status = self.status

    # when a class activated and started, send sms to class students and teacher and admin
    def send_class_started_sms(self):
        # Send sms to class users
        class_users = [item.user.phone for item in self.users.all()]
        for phone in class_users:
            sms_text = SMS_TEXTS['class_users_start'].format(self)
            send_sms(phone, sms_text)

        # Send sms to class teacher
        if self.teacher and hasattr(self.teacher, 'user'):
            sms_text = SMS_TEXTS['class_teacher_start'].format(self)
            send_sms(self.teacher.user.phone, sms_text)

        # Send sms to website admin
        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            sms_text = SMS_TEXTS['class_admin_start'].format(self)
            send_sms(superuser.phone, sms_text)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.status != self.last_status and self.status == 'active':
            self.send_class_started_sms()
