# Generated by Django 4.0 on 2022-04-20 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_comapany_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comapany_details',
            name='Company_phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')]),
        ),
    ]
