from django.contrib.auth import get_user_model
from django.db import models
from Teacher.models import Teacher
from utils.models import CustomModel

User = get_user_model()


class ChatMessage(CustomModel):
    text = models.TextField(verbose_name='متن پیام', max_length=500)
    sender = models.ForeignKey(verbose_name='فرستنده', to=User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(verbose_name='گیرنده', to=User, on_delete=models.CASCADE,
                                 related_name='received_messages')

    class Meta:
        verbose_name = 'چت'
        verbose_name_plural = 'چت ها'

    def __str__(self):
        return self.text or '---'
