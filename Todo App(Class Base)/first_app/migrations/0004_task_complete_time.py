# Generated by Django 4.1.2 on 2022-10-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_task_complete_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
