# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20170325_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='chapter',
            field=models.CharField(default='CHAPTER', max_length=32, verbose_name='章节名'),
        ),
        migrations.AddField(
            model_name='question',
            name='chapter_number',
            field=models.IntegerField(default=0, verbose_name='章节号'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty_degree',
            field=models.IntegerField(default=5, verbose_name='难度系数'),
        ),
    ]
