# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-25 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_ctto_observctto'),
    ]

    operations = [
        migrations.AddField(
            model_name='edp',
            name='ObservEDP',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='odc',
            name='ObservOdc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]