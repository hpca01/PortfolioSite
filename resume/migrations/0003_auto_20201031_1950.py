# Generated by Django 3.1.2 on 2020-10-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resumeproject_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=50, verbose_name='Tool Name')),
                ('tool_color', models.CharField(max_length=50, verbose_name='Tool Color')),
            ],
        ),
        migrations.AddField(
            model_name='resumeproject',
            name='difficulty',
            field=models.IntegerField(default=0, verbose_name='Difficulty'),
        ),
        migrations.AddField(
            model_name='resumeprojectdetail',
            name='tools_used',
            field=models.ManyToManyField(to='resume.ToolsUsed', verbose_name='Tools Used'),
        ),
    ]