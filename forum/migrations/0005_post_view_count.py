# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_user_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='查看次数'),
        ),
    ]
