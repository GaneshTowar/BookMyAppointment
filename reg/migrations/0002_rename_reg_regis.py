# Generated by Django 4.0.2 on 2022-07-24 13:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reg',
            new_name='regis',
        ),
    ]