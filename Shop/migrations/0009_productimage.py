# Generated by Django 4.0.4 on 2022-10-16 09:19

import Shop.models
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import utils.validator


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_product_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('image', models.ImageField(upload_to=Shop.models.upload_image, validators=[utils.validator.validate_file_size], verbose_name='عکس')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Shop.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'گالری تصاویر محصولات',
                'verbose_name_plural': 'گالری تصاویر محصولات ها',
            },
        ),
    ]