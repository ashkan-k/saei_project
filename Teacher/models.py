from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator, RegexValidator
from django.db import models
from django.utils.text import slugify
from utils.models import CustomModel
from utils.validator import validate_file_size
from ACL.models import Role
from ACL.permissions import ROLE_CODES

User = get_user_model()


def upload_resume_file(instance, filename):
    path = 'teachers/resumes/' + slugify(instance.user.phone, allow_unicode=True)
    return path + '/' + filename


###################################################################################

class Teacher(CustomModel):
    user = models.OneToOneField(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='teacher_profile')
    is_approved = models.BooleanField(verbose_name='وضعیت تایید', default=False)
    resume_file = models.FileField(
        verbose_name='فایل رزمه', upload_to=upload_resume_file,
        null=True, blank=True,
        help_text='لطفا فایل رزمه خود را در قالب یکی از پسوند های (jpg,png,txt,docx,doc,pdf) آپلود کنید.',
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg', 'txt', 'doc', 'docx', 'pdf']), validate_file_size]
    )
    bank_account_number = models.CharField(
        null=True,
        blank=True,
        max_length=256,
        help_text="مثال: ۰۱۵۶۳۵۳۰۱۱",
        verbose_name="شماره حساب بانکی",
        validators=[MinLengthValidator(8), MaxLengthValidator(16), RegexValidator(r"[\d۱۲۳۴۵۶۷۸۹۰]{6,18}")]
    )

    class Meta:
        verbose_name = 'مدرس'
        verbose_name_plural = 'مدرس ها'

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
            self.user.change_role(Role.objects.get(code=ROLE_CODES.TEACHER))
            self.user.is_active = self.is_approved
            self.user.save()
        return super().save(*args, **kwargs)

    def get_approved(self):
        return 'تایید شده' if self.is_approved else 'تایید نشده'

    @property
    def get_resume_file(self):
        return self.resume_file.url if self.resume_file else ''

    @property
    def profile_name(self):
        name = '---'
        if self.user and self.user.first_name and self.user.last_name:
            name = self.user.first_name + ' ' + self.user.last_name

        elif self.user and self.user.phone:
            name = self.user.phone

        return name
