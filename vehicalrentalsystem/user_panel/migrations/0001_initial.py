# Generated by Django 4.0.2 on 2022-03-02 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestDate', models.DateTimeField(auto_now_add=True)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Pickup', models.CharField(max_length=20)),
                ('Drop', models.CharField(max_length=20)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('VehicalId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.vehical_registration')),
            ],
        ),
    ]
