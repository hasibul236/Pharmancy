# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20180919_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='batch_no',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='type',
            field=models.CharField(choices=[(b'Tablet', b'Tablet'), (b'Syrup', b'Syrup'), (b'Injection', b'Injection'), (b'Shampoo', b'Shampoo'), (b'Capsule', b'Capsule'), (b'Not Define', b'Not Define')], default=b'Not Define', max_length=25),
        ),
    ]
