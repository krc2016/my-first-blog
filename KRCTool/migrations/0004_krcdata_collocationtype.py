# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KRCTool', '0003_auto_20160104_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='krcdata',
            name='collocationType',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
