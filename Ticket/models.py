from django.contrib.auth import get_user_model
from django.db import models
from Teacher.models import Teacher
from Ticket.helpers import TicketStatus, TicketStatusClass
from utils.models import CustomModel

User = get_user_model()


def file_upload(instance, filename):
    return "tickets/{}/{}".format(instance.user_id, filename)


##############################################################

class TicketCategory(CustomModel):
    title = models.CharField(
        unique=True,
        max_length=150,
        verbose_name="عنوان",
    )

    class Meta:
        verbose_name = 'دسته بندی تیکت'
        verbose_name_plural = 'دسته بندی تیکت ها'

    def __str__(self):
        return self.title or '---'


class Ticket(CustomModel):
    user = models.ForeignKey(
        to=User,
        related_name="tickets",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        null=True,
        blank=True,
        to=TicketCategory,
        related_name="tickets",
        verbose_name="دسته بندی تیکت",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=100,
        verbose_name="عنوان",
    )
    status = models.CharField(
        max_length=40,
        verbose_name="وضعیت",
        default=TicketStatus.WAITING,
        choices=TicketStatus.CHOICES,
    )
    text = models.TextField(
        verbose_name="متن پیام"
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to=file_upload,
        verbose_name="فایل ضمیمه",
    )

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.title or '---'

    def answered(self):
        self.status = TicketStatus.ANSWERED
        self.save()

    def waited(self):
        self.status = TicketStatus.WAITING
        self.save()

    @property
    def get_status(self):
        return dict(TicketStatus.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(TicketStatusClass.CHOICES).get(self.status, '')

    @property
    def get_file(self):
        return self.file.url if self.file else ''


class TicketAnswer(CustomModel):
    user = models.ForeignKey(
        to=User,
        related_name="ticket_answers",
        on_delete=models.CASCADE,
    )
    ticket = models.ForeignKey(
        to=Ticket,
        verbose_name='پیام',
        related_name="answers",
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="متن پیام"
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to=file_upload,
        verbose_name="فایل ضمیمه",
    )

    class Meta:
        verbose_name = 'پاسخ های تیکت'
        verbose_name_plural = 'پاسخ های تیکت ها'

    def __str__(self):
        return self.text or '---'

    def save(self, *args, **kwargs):
        if self.ticket.user != self.user:
            self.ticket.answered()
        else:
            self.ticket.waited()
        return super().save(*args, **kwargs)

    @property
    def get_file(self):
        return self.file.url if self.file else ''
