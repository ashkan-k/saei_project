from django.contrib.auth import get_user_model
from django.db import models
from Class.models import Class
from media.helpers import POLL_QUESTION_OPTIONS
from utils.models import CustomModel

User = get_user_model()


class Poll(CustomModel):
    """ فرم نظرسنجی """
    class_item = models.ForeignKey(verbose_name='کلاس', to=Class, on_delete=models.CASCADE, related_name='polls')
    is_active = models.BooleanField(verbose_name='وضعیت فعال', default=False)

    class Meta:
        verbose_name = 'فرم نظرسنجی'
        verbose_name_plural = 'فرم نظرسنجی ها'

    def __str__(self):
        return self.class_item.__str__() or '---'


class UserPoll(CustomModel):
    """ پاسخنامه کاربر """
    user = models.ForeignKey(
        to=User,
        related_name='polls',
        verbose_name='کاربر',
        on_delete=models.CASCADE,
    )
    poll = models.ForeignKey(
        to=Poll,
        verbose_name='نظرسنجی',
        on_delete=models.CASCADE,
        related_name='user_polls',
    )
    presentation_of_the_lesson_plan = models.CharField(verbose_name='ارئه طرح درس و معرفی منابع و رفرنس های معتبر', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    mastery_of_the_teacher_on_the_subject_of_the_lesson = models.CharField(verbose_name='تسلط استاد بر موضوع درس', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    way_of_expression = models.CharField(verbose_name='تسلط استاد بر موضوع درس', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    method_of_expression = models.CharField(verbose_name='شیوه بیان، تفهیم و انتقال مطالب درسی', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    teaching_method = models.CharField(verbose_name='شیوه تدریس و بکار گیری امکانات کمک آموزشی موجود', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    participation = models.CharField(verbose_name='جلب مشارکت و ایجاد انگیزه در مباحث درسی', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    responsiveness = models.CharField(verbose_name='اهمیت دادن به پاسخگویی سوالات درسی دانشجویان', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    being_scientific = models.CharField(verbose_name='میزان علمی بودن محتوای کلاس أموزشی', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    order_and_time = models.CharField(verbose_name='نحوه مدیریت کلاس (نظم و زمان)', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    arrivals_and_departures = models.CharField(verbose_name='ورود و خروج به موقع به کلاس', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)
    social_etiquette_and_behavior = models.CharField(verbose_name='آداب و رفتار اجتماعی با دانشجویان و رفتار متقابل', max_length=255, choices=POLL_QUESTION_OPTIONS.CHOICES)

    class Meta:
        verbose_name = 'پاسخ فرم نظرسنجی'
        verbose_name_plural = 'پاسخ فرم نظرسنجی ها'

    def __str__(self):
        return f'{self.user}, {self.poll}'
