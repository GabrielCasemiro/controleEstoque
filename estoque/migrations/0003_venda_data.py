# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-15 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20190415_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
