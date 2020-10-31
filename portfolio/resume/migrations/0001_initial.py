# Generated by Django 3.1.2 on 2020-10-31 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('ongoing', models.BooleanField(verbose_name='Ongoing')),
                ('quick_blurb', models.CharField(max_length=200, verbose_name='Quick Blurb')),
                ('long_description', models.TextField(blank=True, verbose_name='Long Description')),
                ('git_link', models.CharField(max_length=200, verbose_name='Git Link')),
                ('main_img', models.ImageField(upload_to='resume', verbose_name='Image Upload')),
            ],
            options={
                'verbose_name': 'ResumeProject',
                'verbose_name_plural': 'ResumeProjects',
            },
        ),
        migrations.CreateModel(
            name='ResumeProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_short', models.CharField(max_length=100, verbose_name='Short Detail')),
                ('explanation', models.CharField(max_length=250, verbose_name='Longer Explanation')),
                ('associated_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeproject')),
            ],
            options={
                'verbose_name': 'ResumeProjectDetail',
                'verbose_name_plural': 'ResumeProjectDetails',
            },
        ),
    ]
