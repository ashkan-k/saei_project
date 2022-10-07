# Generated by Django 4.0.4 on 2022-05-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('name', models.CharField(max_length=50, verbose_name='نام نمایشی')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='عنوان انگلیسی')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'دسترسی',
                'verbose_name_plural': 'دسترسی ها',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('name', models.CharField(max_length=50, verbose_name='نام نمایشی')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='عنوان انگلیسی')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('permissions', models.ManyToManyField(blank=True, related_name='role', to='ACL.permission', verbose_name='نقش ها')),
            ],
            options={
                'verbose_name': 'نقش',
                'verbose_name_plural': 'نقش ها',
            },
        ),
    ]
