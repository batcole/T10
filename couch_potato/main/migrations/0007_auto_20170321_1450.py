# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170321_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(default='undescribed', max_length=1000),
        ),
    ]