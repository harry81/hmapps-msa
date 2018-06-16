# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-06 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0009_auto_20170606_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='location',
            field=models.OneToOneField(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='earth.Location'),
        ),
    ]