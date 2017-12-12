# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-21 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=10, max_digits=10)),
                ('lon', models.DecimalField(decimal_places=10, max_digits=10)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
    ]
