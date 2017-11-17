# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-17 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_tank_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phhistory',
            name='tank_id',
        ),
        migrations.RemoveField(
            model_name='temphistory',
            name='tank_id',
        ),
        migrations.RemoveField(
            model_name='waterchangehistory',
            name='tank_id',
        ),
        migrations.AddField(
            model_name='phhistory',
            name='tank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Tank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphistory',
            name='tank',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.Tank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waterchangehistory',
            name='tank',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.Tank'),
            preserve_default=False,
        ),
    ]
