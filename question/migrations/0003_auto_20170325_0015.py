# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20170325_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='subjct',
            new_name='subject',
        ),
    ]