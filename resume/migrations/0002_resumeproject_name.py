# Generated by Django 3.1.2 on 2020-10-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeproject',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
