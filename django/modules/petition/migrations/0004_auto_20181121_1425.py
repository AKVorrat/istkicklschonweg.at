# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0003_auto_20181120_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='token',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]