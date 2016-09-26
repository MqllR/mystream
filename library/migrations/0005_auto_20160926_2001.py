# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 20:01
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_stream_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='encoded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stream',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='stream',
            name='movie',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/tmp/'), upload_to='tmp/'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
