# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KRCTool', '0006_auto_20160217_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='valider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oui', models.BooleanField(default=True)),
                ('non', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='krcrequest',
            name='case_val',
            field=models.ManyToManyField(to='KRCTool.valider'),
        ),
    ]
