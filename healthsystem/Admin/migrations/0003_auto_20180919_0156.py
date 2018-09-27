# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_medicine_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='generic',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
