# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0010_exercisehistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercisehistory',
            old_name='submitOptions',
            new_name='submit_options',
        ),
        migrations.RenameField(
            model_name='exercisehistory',
            old_name='submitTime',
            new_name='submit_time',
        ),
    ]
