# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-05 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0004_item_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='publisher',
            field=models.CharField(choices=[('h', 'hanis'), ('m', 'mk')], max_length=1),
        ),
    ]
