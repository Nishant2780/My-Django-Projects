# Generated by Django 4.1.2 on 2022-10-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='User',
        ),
        migrations.AlterField(
            model_name='task',
            name='Complete_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
