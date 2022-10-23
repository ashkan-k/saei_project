from django.contrib.auth import get_user_model
from django.db import models

from ACL.models import Role
from ACL.permissions import ROLE_CODES
from utils.models import CustomModel
from utils.validator import mobile_regex

User = get_user_model()


class Student(CustomModel):
    user = models.OneToOneField(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='student_profile')
    is_approved = models.BooleanField(verbose_name='وضعیت تایید', default=False)
    parent_phone = models.CharField(verbose_name="شماره موبایل والد", max_length=11, validators=[mobile_regex],
                             null=True)

    class Meta:
        verbose_name = 'هنرجو'
        verbose_name_plural = 'هنرجویان'

    def __str__(self):
        return self.user.full_name if self.user else '---'

    def approve(self):
        self.is_approved = True
        if self.user:
            self.user.is_active = True
            self.user.save()
        self.save()

    def reject(self):
        self.is_approved = False
        self.save()

    def save(self, *args, **kwargs):
        if self.user:
            self.user.change_role(Role.objects.get(code=ROLE_CODES.STUDENT))
            self.user.is_active = self.is_approved
            self.user.save()
        return super().save(*args, **kwargs)

    def get_approved(self):
        return 'تایید شده' if self.is_approved else 'تایید نشده'
