# Generated by Django 4.0 on 2022-04-20 12:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comapany_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comapany_Name', models.CharField(max_length=15)),
                ('Company_address', models.CharField(max_length=60)),
                ('Company_phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{6}$')])),
                ('gst_numbe', models.CharField(max_length=15)),
            ],
        ),
    ]