# Generated by Django 2.2.15 on 2022-08-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0032_auto_20220811_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_endtime',
            field=models.DateTimeField(verbose_name='End date of the event: '),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_starttime',
            field=models.DateTimeField(verbose_name='Start Date of the event: '),
        ),
    ]
