# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180112_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]