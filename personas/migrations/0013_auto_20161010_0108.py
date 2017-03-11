# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-10 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0012_question_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctto',
            name='LocalCtto',
            field=models.CharField(blank=True, choices=[('Local', 'Local'), ('Nacional', 'Nacional'), ('Extranjero', 'Extranjero')], default='Nacional', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('Local', 'Local'), ('Nacional', 'Nacional'), ('Extranjero', 'Extranjero')], max_length=255),
        ),
    ]
