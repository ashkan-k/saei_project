# Generated by Django 4.0.4 on 2022-10-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_alter_student_created_at_alter_student_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='intro_method',
            field=models.CharField(blank=True, choices=[('website', 'از طریق سایت'), ('ads', 'تبلیغات تراکتی'), ('social', 'اپلیکیشن های مجازی'), ('sms_ads', 'پیامک تبلیغاتی'), ('students_and_teachers', 'دانش اموزان و همکاران')], max_length=100, null=True, verbose_name='نحوه آشنایی'),
        ),
    ]
