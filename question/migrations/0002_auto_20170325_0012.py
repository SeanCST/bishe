# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='difficultyDegree',
            new_name='difficulty_degree',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='subjctNumber',
            new_name='subject_number',
        ),
    ]
