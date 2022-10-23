# Generated by Django 4.0.4 on 2022-10-23 20:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_student_parent_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parent_phone',
            field=models.CharField(max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='شماره موبایل معتبر نیست.', regex='(^\\+?(09|98|0)?(9([0-9]{9}))$)')], verbose_name='شماره موبایل والد'),
        ),
    ]