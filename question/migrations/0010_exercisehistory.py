# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20170331_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=50, verbose_name='学号')),
                ('question_numbers', models.CharField(max_length=50, verbose_name='题目序号')),
                ('submitOptions', models.CharField(max_length=50, verbose_name='提交选项')),
                ('score', models.CharField(max_length=20, verbose_name='分数')),
                ('submitTime', models.DateTimeField(auto_now=True, verbose_name='提交时间')),
            ],
        ),
    ]
