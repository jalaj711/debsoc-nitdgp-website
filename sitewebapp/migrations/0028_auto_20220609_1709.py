# Generated by Django 2.2.15 on 2022-06-09 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0027_access_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_status',
        ),
        migrations.AddField(
            model_name='event',
            name='event_endtime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 17, 9, 30, 253163), verbose_name='End date of the event: '),
        ),
        migrations.AddField(
            model_name='event',
            name='event_starttime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 9, 17, 9, 30, 253151), verbose_name='Start Date of the event: '),
        ),
    ]
