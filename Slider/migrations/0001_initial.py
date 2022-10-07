# Generated by Django 4.0.4 on 2022-05-30 14:15

import Slider.models
from django.db import migrations, models
import utils.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=Slider.models.upload_image, validators=[utils.validator.validate_file_size], verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]
