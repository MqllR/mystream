# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='url',
        ),
        migrations.AddField(
            model_name='stream',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
    ]