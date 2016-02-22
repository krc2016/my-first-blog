# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KRCTool', '0002_auto_20160102_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='krcdata',
            name='krcrequest',
        ),
        migrations.AddField(
            model_name='krcdata',
            name='ttermSource',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='krcdata',
            name='ttermTarget',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='krcrequest',
            name='corpus',
            field=models.CharField(choices=[('Vulcanologie', 'Vulcanologie'), ('Diab\xe8te', 'Diab\xe8te'), ('Cancer du sein', 'Cancer du sein')], default='Vulcanologie', max_length=20),
        ),
        migrations.AlterField(
            model_name='krcrequest',
            name='translSens',
            field=models.CharField(choices=[('EN-FR', 'EN-FR'), ('FR-EN', 'FR-EN')], default='EN-FR', max_length=20),
        ),
    ]
