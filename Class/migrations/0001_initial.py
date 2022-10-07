# Generated by Django 4.0.4 on 2022-05-31 08:06

import Class.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teacher', '0002_teacher_resume_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('desc', models.TextField(max_length=500, verbose_name='توضیحات')),
                ('amount', models.PositiveIntegerField(verbose_name='شهریه (تومان)')),
                ('users_limit', models.PositiveIntegerField(blank=True, null=True, verbose_name='تعداد مجاز شرکت کنندگان')),
                ('status', models.CharField(choices=[('active', 'فعال'), ('deactive', 'غیرفعال')], default='active', max_length=50, verbose_name='وضعیت')),
                ('start_date', models.DateTimeField(verbose_name='تاریخ شروع')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=Class.models.upload_cover_file, validators=[utils.validator.validate_file_size], verbose_name='عکس (کاور)')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='Teacher.teacher', verbose_name='مدرس')),
            ],
            options={
                'verbose_name': 'کلاس',
                'verbose_name_plural': 'کلاس ها',
            },
        ),
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('class_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='Class.class', verbose_name='کلاس')),
            ],
            options={
                'verbose_name': 'حضور و غیاب ها',
                'verbose_name_plural': 'حضور و غیاب ها',
            },
        ),
        migrations.CreateModel(
            name='ClassUserAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('status', models.CharField(choices=[('present', 'حاضر'), ('absent', 'غایب')], max_length=50, verbose_name='وضعیت')),
                ('class_attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Class.classattendance', verbose_name='کلاس')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کاربران حضور و غیاب',
                'verbose_name_plural': 'کاربران حضور و غیاب',
            },
        ),
        migrations.CreateModel(
            name='ClassUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('status', models.CharField(choices=[('active', 'فعال'), ('deactive', 'غیرفعال')], default='active', max_length=50, verbose_name='وضعیت')),
                ('class_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Class.class', verbose_name='کلاس')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کاربران کلاس ها',
                'verbose_name_plural': 'کاربران کلاس ها',
            },
        ),
    ]
