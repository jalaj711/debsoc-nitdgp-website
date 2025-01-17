# Generated by Django 2.2.15 on 2022-08-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0033_auto_20220819_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakeDeBaitRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_email', models.EmailField(max_length=254, unique=True)),
                ('member_1_name', models.TextField()),
                ('member_1_number', models.CharField(max_length=10)),
                ('member_2_name', models.TextField()),
                ('member_2_number', models.CharField(max_length=10)),
                ('member_3_name', models.TextField()),
                ('member_3_number', models.CharField(max_length=10)),
                ('member_4_name', models.TextField()),
                ('member_4_number', models.CharField(max_length=10)),
            ],
        ),
    ]
