# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeSheetApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
