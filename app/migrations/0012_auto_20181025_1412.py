# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-25 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
