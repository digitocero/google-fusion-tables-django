# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-21 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20170921_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=30, max_digits=40),
        ),
        migrations.AlterField(
            model_name='location',
            name='lon',
            field=models.DecimalField(decimal_places=30, max_digits=40),
        ),
    ]
