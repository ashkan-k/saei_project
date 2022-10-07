from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from Course.helpers import COURSE_STATUS, CourseStatusStatusClass, COURSE_USER_STATUS, CourseUserStatusStatusClass
from utils.models import CustomModel
from Teacher.models import Teacher
from django.utils.text import slugify

from utils.validator import validate_file_size

User = get_user_model()


def upload_cover_file(instance, filename):
    path = 'courses/cover/' + slugify(instance.title, allow_unicode=True)
    return path + '/' + filename


class Course(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    desc = models.TextField(verbose_name='توضیحات', max_length=500)
    amount = models.PositiveIntegerField(verbose_name='قیمت (تومان)')
    users_limit = models.PositiveIntegerField(verbose_name='تعداد مجاز شرکت کنندگان')
    status = models.CharField(verbose_name='وضعیت', default='draft', choices=COURSE_STATUS.CHOICES, max_length=50)
    teacher = models.ForeignKey(verbose_name='مدرس', to=Teacher, on_delete=models.CASCADE, related_name='courses')
    start_date = models.DateTimeField(verbose_name='تاریخ شروع')

    cover = models.ImageField(
        verbose_name='عکس (کاور)', upload_to=upload_cover_file,
        # null=True, blank=True,
        validators=[validate_file_size]
    )

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return self.title or '---'

    @property
    def get_status(self):
        return dict(COURSE_STATUS.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(CourseStatusStatusClass.CHOICES).get(self.status, '')

    def get_cover(self):
        return self.cover.url if self.cover else '/static/admin_panel/assets/img/class.png'


class CourseUser(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='courses')
    course = models.ForeignKey(verbose_name='دوره', to=Course, on_delete=models.CASCADE, related_name='users')
    status = models.CharField(verbose_name='وضعیت', default='active', choices=COURSE_USER_STATUS.CHOICES, max_length=50)

    class Meta:
        verbose_name = 'دوره های کاربران'
        verbose_name_plural = 'دوره های کاربران ها'

    def __str__(self):
        return f"{self.user or '---'}-{self.course or '---'}"

    @property
    def get_status(self):
        return dict(COURSE_USER_STATUS.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(CourseUserStatusStatusClass.CHOICES).get(self.status, '')