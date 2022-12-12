from django.contrib.auth import get_user_model
from django.db import models
from Teacher.models import Teacher
from utils.models import CustomModel
from utils.validator import validate_file_size

User = get_user_model()


class ChatMessage(CustomModel):
    text = models.TextField(verbose_name='متن پیام', max_length=500, null=True,
        blank=True)
    sender = models.ForeignKey(verbose_name='فرستنده', to=User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(verbose_name='گیرنده', to=User, on_delete=models.CASCADE,
                                 related_name='received_messages')
    file = models.FileField(
        verbose_name='فایل پیام',
        max_length=500, null=True,
        blank=True, upload_to='chats',
        validators=[validate_file_size]
    )

    class Meta:
        verbose_name = 'چت'
        verbose_name_plural = 'چت ها'

    def __str__(self):
        return self.text or '---'

    def get_file(self):
        return self.file.url if self.file else None
