# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20180307_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='EstaActivo',
            field=models.CharField(choices=[('No', 'No'), ('Si', 'Si')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]