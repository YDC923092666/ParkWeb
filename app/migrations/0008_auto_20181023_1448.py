# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-23 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181019_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='showberth',
            name='controlTotalNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='controlclass1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='controlclass2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='controlclass3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='remainTotalNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='remainclass1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='remainclass2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='showberth',
            name='remainclass3',
            field=models.IntegerField(default=0),
        ),
    ]