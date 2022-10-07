from django.db import models

from utils.models import CustomModel


class Help(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=255)
    desc = models.TextField(verbose_name='توضیحات', max_length=500)

    class Meta:
        verbose_name = 'متون راهنما'
        verbose_name_plural = 'متون راهنما'

    def __str__(self):
        return self.title or '---'
