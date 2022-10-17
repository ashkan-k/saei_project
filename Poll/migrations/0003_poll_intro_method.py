# Generated by Django 4.0.4 on 2022-10-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_rename_is_approved_poll_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='intro_method',
            field=models.CharField(blank=True, choices=[('website', 'از طریق سایت'), ('ads', 'تبلیغات تراکتی'), ('social', 'اپلیکیشن های مجازی'), ('sms_ads', 'پیامک تبلیغاتی'), ('students_and_teachers', 'دانش اموزان و همکاران')], max_length=100, null=True, verbose_name='نحوه آشنایی'),
        ),
    ]