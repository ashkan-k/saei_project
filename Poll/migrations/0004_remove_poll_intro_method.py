# Generated by Django 4.0.4 on 2022-10-17 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0003_poll_intro_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='intro_method',
        ),
    ]
