# Generated by Django 3.1.3 on 2020-11-07 16:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201031_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeproject',
            name='main_img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image Upload'),
        ),
    ]
