# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170405_0958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'get_latest_by': ('id',), 'permissions': (('view_task', 'View Task'), ('stop_task', 'Stop Task'), ('run_task', 'Run Task'), ('replay_task', 'Replay Task'))},
        ),
    ]
