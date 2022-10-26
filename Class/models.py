import jdatetime
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django_jalali.db import models as jmodels
from Class.helpers import CLASS_STATUS, ClassStatusStatusClass, CLASS_USER_STATUS, ClassUserStatusStatusClass, \
    CLASS_USER_ATTENDANCE_STATUS, ClassUserStatusAttendanceStatusClass
from Class.mixins import ClassStartedSmsMixin
from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from utils.models import CustomModel
from Teacher.models import Teacher
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from utils.validator import validate_file_size
from django.utils.crypto import get_random_string

User = get_user_model()


def upload_cover_file(instance, filename):
    path = 'classes/cover/' + slugify(instance.title, allow_unicode=True)
    return path + '/' + filename


"""Class And Class Users Models"""


class Class(ClassStartedSmsMixin, CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    slug = models.SlugField(verbose_name='نامک (slug)', max_length=255, allow_unicode=True, null=True, blank=True)
    desc = models.TextField(verbose_name='توضیحات', max_length=500)
    amount = models.PositiveBigIntegerField(verbose_name='شهریه (تومان)')
    users_limit = models.PositiveIntegerField(verbose_name='تعداد مجاز شرکت کنندگان', null=True, blank=True)
    status = models.CharField(verbose_name='وضعیت', default='active', choices=CLASS_STATUS.CHOICES, max_length=50)
    teacher = models.ForeignKey(verbose_name='مدرس', to=Teacher, on_delete=models.CASCADE, related_name='classes')
    # start_date = jmodels.jDateField(verbose_name='تاریخ شروع', null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True, verbose_name="زمان شروع کلاس")
    end_time = models.TimeField(null=True, blank=True, verbose_name="زمان پایان کلاس")
    cover = models.ImageField(
        verbose_name='عکس (کاور)', upload_to=upload_cover_file,
        null=True, blank=True,
        validators=[validate_file_size]
    )
    is_special = models.BooleanField(verbose_name='ایا ویژه است؟', default=False)
    is_show_in_slider = models.BooleanField(verbose_name='آیا در صفحه اصلی نمایش داده شود؟', default=False)

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'

    def __str__(self):
        return self.title or '---'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, True)

        if self.slug:
            qs = Class.objects.filter(
                slug=self.slug)
            if self.pk:
                qs = qs.exclude(id=self.pk)
            if qs.exists():
                self.slug = str(get_random_string(length=10))
        return super().save(*args, **kwargs)

    @property
    def get_status(self):
        return dict(CLASS_STATUS.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(ClassStatusStatusClass.CHOICES).get(self.status, '')

    def get_cover(self):
        return self.cover.url if self.cover else '/static/admin_panel/assets/img/class.png'


class ClassUser(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='classes')
    class_item = models.ForeignKey(verbose_name='کلاس', to=Class, on_delete=models.CASCADE, related_name='users')
    status = models.CharField(verbose_name='وضعیت', default='active', choices=CLASS_USER_STATUS.CHOICES, max_length=50)
    adobe_connect_link = models.URLField(verbose_name='لینک ادوب کانکت', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربران کلاس ها'
        verbose_name_plural = 'کاربران کلاس ها'

    def __str__(self):
        return f"{self.user or '---'}-{self.class_item or '---'}"

    @property
    def get_status(self):
        return dict(CLASS_USER_STATUS.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(ClassUserStatusStatusClass.CHOICES).get(self.status, '')


"""Class Attendance Models"""


class ClassAttendance(CustomModel):
    class_item = models.ForeignKey(verbose_name='کلاس', to=Class, on_delete=models.CASCADE, related_name='attendances')
    date = jmodels.jDateField(verbose_name='تاریخ')

    class Meta:
        verbose_name = 'حضور و غیاب ها'
        verbose_name_plural = 'حضور و غیاب ها'

    def __str__(self):
        return f"{self.class_item or '---'}"


class ClassUserAttendance(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='attendances')
    class_attendance = models.ForeignKey(verbose_name='کلاس', to=ClassAttendance, on_delete=models.CASCADE,
                                         related_name='users')
    desc = models.TextField(verbose_name='توضیحات', max_length=500, null=True, blank=True)
    status = models.CharField(verbose_name='وضعیت', choices=CLASS_USER_ATTENDANCE_STATUS.CHOICES, max_length=50)

    class Meta:
        verbose_name = 'کاربران حضور و غیاب'
        verbose_name_plural = 'کاربران حضور و غیاب'

    def __str__(self):
        return f"{self.user or '---'}-{self.class_attendance or '---'}"

    @property
    def get_status(self):
        return dict(CLASS_USER_ATTENDANCE_STATUS.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(ClassUserStatusAttendanceStatusClass.CHOICES).get(self.status, '')
