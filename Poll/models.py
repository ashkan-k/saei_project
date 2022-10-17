from django.contrib.auth import get_user_model
from django.db import models
from Class.models import Class
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
    title = models.CharField(verbose_name='عنوان', max_length=255)
    text = models.TextField(verbose_name='توضیحات', max_length=500)

    class Meta:
        verbose_name = 'پاسخ فرم نظرسنجی'
        verbose_name_plural = 'پاسخ فرم نظرسنجی ها'

    def __str__(self):
        return f'{self.user}, {self.poll}'
