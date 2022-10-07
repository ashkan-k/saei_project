# Generated by Django 4.0.4 on 2022-06-01 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Teacher', '0003_alter_teacher_created_at_alter_teacher_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('text', models.TextField(max_length=500, verbose_name='متن پیام')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='Teacher.teacher', verbose_name='مدرس')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='فرستنده')),
            ],
            options={
                'verbose_name': 'چت',
                'verbose_name_plural': 'چت ها',
            },
        ),
    ]
