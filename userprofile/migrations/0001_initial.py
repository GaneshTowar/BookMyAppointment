# Generated by Django 4.0.2 on 2022-07-25 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('serviceprovider', models.BooleanField(blank=True, null=True)),
                ('opensat', models.TimeField(null=True)),
                ('closesat', models.TimeField(null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('noappointments', models.IntegerField(blank=True, null=True)),
                ('visitfee', models.IntegerField(blank=True, null=True)),
                ('occupation', models.TextField(blank=True, max_length=500)),
                ('city', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]