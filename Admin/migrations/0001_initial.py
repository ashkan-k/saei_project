# Generated by Django 4.0.4 on 2022-11-05 19:14

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('link', models.TextField(verbose_name='لینک')),
            ],
            options={
                'verbose_name': 'عکس داشبورد',
                'verbose_name_plural': 'عکس داشبورد ها',
            },
        ),
    ]