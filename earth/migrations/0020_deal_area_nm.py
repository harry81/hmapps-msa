# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0019_auto_20170628_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='area_nm',
            field=models.CharField(default=b'', max_length=32, verbose_name='\uc9c0\uc5ed\uc774\ub984'),
        ),
    ]
