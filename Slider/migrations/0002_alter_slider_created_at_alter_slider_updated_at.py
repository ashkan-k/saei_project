# Generated by Django 4.0.4 on 2022-05-31 10:03

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='updated_at',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
    ]
