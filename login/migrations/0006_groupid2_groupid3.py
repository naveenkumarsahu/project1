# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20160905_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupid2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactName', models.CharField(max_length=15)),
                ('MobileNo', models.BigIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Groupid3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContactName', models.CharField(max_length=15)),
                ('MobileNo', models.BigIntegerField(max_length=10)),
            ],
        ),
    ]
