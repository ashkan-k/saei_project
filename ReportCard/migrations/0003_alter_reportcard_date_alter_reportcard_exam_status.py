# Generated by Django 4.0.4 on 2022-08-30 10:38

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportCard', '0002_alter_reportcard_date_alter_reportcard_exam_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date',
            field=django_jalali.db.models.jDateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='exam_status',
            field=models.CharField(blank=True, choices=[('pass', 'PASS'), ('cp', '.C.P'), ('fail', 'FAIL')], max_length=255, null=True, verbose_name='Exam Status'),
        ),
    ]
