# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160411_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
