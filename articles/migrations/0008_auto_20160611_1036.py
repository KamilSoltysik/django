# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-11 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
