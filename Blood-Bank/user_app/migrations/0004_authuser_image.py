# Generated by Django 4.0.1 on 2022-02-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
