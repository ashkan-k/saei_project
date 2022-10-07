# Generated by Django 4.0.4 on 2022-05-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('draft', 'در انتظار'), ('draft', 'منتشر شده'), ('finished', 'پایان یافته')], default='draft', max_length=50, verbose_name='وضعیت'),
        ),
    ]
