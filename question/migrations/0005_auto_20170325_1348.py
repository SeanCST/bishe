# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20170325_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_time',
            field=models.DateTimeField(auto_now=True, verbose_name='收录时间'),
        ),
    ]
