# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0004_auto_20181121_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='emails_sent',
            field=models.IntegerField(default=0),
        ),
    ]