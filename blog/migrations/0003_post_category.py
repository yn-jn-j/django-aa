# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-29 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
