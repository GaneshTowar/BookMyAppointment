# Generated by Django 4.0.2 on 2022-07-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_rename_reg_regis'),
    ]

    operations = [
        migrations.AddField(
            model_name='regis',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='regis',
            name='time',
            field=models.FloatField(null=True),
        ),
    ]
