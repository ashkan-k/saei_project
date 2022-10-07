from django.contrib.auth import get_user_model
from django.db import models
from ACL.models import Role
from Class.models import Class
from ReportCard.helpers import REPORT_CARD_TYPE, EXAM_STATUS
from utils.models import CustomModel
from django_jalali.db import models as jmodels

User = get_user_model()


class ReportCard(CustomModel):
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='report_cards')
    title = models.CharField(verbose_name='عنوان', max_length=255, null=True, blank=True)
    class_item = models.ForeignKey(verbose_name='کلاس', to=Class, on_delete=models.CASCADE, related_name='report_cards')

    certify_that = models.CharField(verbose_name='This is to certify that', max_length=255, null=True, blank=True)
    awarded = models.CharField(verbose_name='has been awarded', max_length=255, null=True, blank=True)
    in_the = models.CharField(verbose_name='in the', max_length=255, null=True, blank=True)
    on = models.CharField(verbose_name='on', max_length=255, null=True, blank=True)
    place_of_entry = models.CharField(verbose_name='place of Entry', max_length=255, null=True, blank=True)
    refrence_number = models.CharField(verbose_name='Refrence Number', max_length=255, null=True, blank=True)

    proudly_presented = models.CharField(verbose_name='This certificate is proudly presented to', max_length=255,
                                         null=True, blank=True)
    completed_term = models.CharField(verbose_name='having successfully completed a term of ?', max_length=255,
                                      null=True, blank=True)
    class_attendance = models.CharField(verbose_name='Class Attendance', max_length=255, null=True, blank=True)
    class_activity = models.CharField(verbose_name='Class Activity', max_length=255, null=True, blank=True)
    homework = models.CharField(verbose_name='Homework', max_length=255, null=True, blank=True)
    workbook = models.CharField(verbose_name='Workbook', max_length=255, null=True, blank=True)
    listening = models.CharField(verbose_name='Listening', max_length=255, null=True, blank=True)
    speaking = models.CharField(verbose_name='Speaking', max_length=255, null=True, blank=True)
    reading = models.CharField(verbose_name='Reading', max_length=255, null=True, blank=True)
    writing = models.CharField(verbose_name='Writing', max_length=255, null=True, blank=True)
    midterm_score = models.CharField(verbose_name='Midterm Score', max_length=255, null=True, blank=True)
    final_exam = models.CharField(verbose_name='Final Exam', max_length=255, null=True, blank=True)
    oral_score = models.CharField(verbose_name='Oral Score', max_length=255, null=True, blank=True)
    overall = models.CharField(verbose_name='Overall', max_length=255, null=True, blank=True)
    exam_status = models.CharField(verbose_name='Exam Status', choices=EXAM_STATUS.CHOICES, max_length=255, null=True,
                                   blank=True)
    date = jmodels.jDateField(verbose_name='Date', null=True, blank=True)
    type = models.CharField(verbose_name='نوع کارنامه', max_length=255, choices=REPORT_CARD_TYPE.CHOICES)

    class Meta:
        verbose_name = 'کارنامه'
        verbose_name_plural = 'کارنامه ها'

    def __str__(self):
        return f"{self.user}-{self.class_item}" or '---'

    @property
    def get_type(self):
        return dict(REPORT_CARD_TYPE.CHOICES).get(self.type, '')

    def show_report_card_pdf(self):
        pass  # TOD Create CardReport PDF
