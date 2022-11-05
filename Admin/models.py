from django.db import models

from utils.models import CustomModel


class DashboardImage(CustomModel):
    link = models.TextField(verbose_name='لینک')

    class Meta:
        verbose_name = 'عکس داشبورد'
        verbose_name_plural = 'عکس داشبورد ها'

    def __str__(self):
        return self.link or '---'
