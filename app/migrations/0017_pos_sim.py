# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-26 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0016_auto_20181029_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='POS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('城西片区', '城西片区'), ('城东片区', '城东片区'), ('城南片区', '城南片区'), ('高新片区', '高新片区'), ('游仙片区', '游仙片区'), ('科创园片区', '科创园片区'), ('库存中', '库存中'), ('待返修', '待返修'), ('返修中', '返修中'), ('已遗失', '已遗失'), ('已损坏', '已损坏'), ('其他', '其他')], default='库存中', max_length=10)),
                ('people', models.CharField(max_length=20)),
                ('POS_Model', models.CharField(max_length=20)),
                ('POS_ID', models.CharField(max_length=50)),
                ('POS_SN', models.CharField(max_length=50)),
                ('POS_Battery', models.BooleanField(default=True)),
                ('POS_Charger', models.BooleanField(default=True)),
                ('TF', models.BooleanField(default=True)),
                ('printer', models.BooleanField(default=True)),
                ('printer_Charger', models.BooleanField(default=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
                ('changeTime', models.DateTimeField(auto_now=True)),
                ('createUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createPOSUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'POS管理',
                'verbose_name_plural': 'POS管理',
                'permissions': (('can_edit_hardware', '是否可以编辑POS信息'),),
            },
        ),
        migrations.CreateModel(
            name='SIM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('城西片区', '城西片区'), ('城东片区', '城东片区'), ('城南片区', '城南片区'), ('高新片区', '高新片区'), ('游仙片区', '游仙片区'), ('科创园片区', '科创园片区'), ('库存中', '库存中'), ('已遗失', '已遗失'), ('已损坏', '已损坏'), ('其他', '其他')], default='库存中', max_length=10)),
                ('SIM_ICCID', models.CharField(max_length=50)),
                ('SIM_Company', models.CharField(max_length=10)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
                ('changeTime', models.DateTimeField(auto_now=True)),
                ('createUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createSIMUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SIM管理',
                'verbose_name_plural': 'SIM管理',
                'permissions': (('can_edit_SIM', '是否可以编辑SIM信息'),),
            },
        ),
    ]
