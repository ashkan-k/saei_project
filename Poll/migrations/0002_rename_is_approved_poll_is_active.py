# Generated by Django 4.0.4 on 2022-10-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='is_approved',
            new_name='is_active',
        ),
    ]