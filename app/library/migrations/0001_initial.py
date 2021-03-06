# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('cmd', models.CharField(max_length=255)),
                ('directory', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('movie', models.CharField(max_length=255, null=True)),
                ('encoded', models.BooleanField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Category')),
                ('quality', models.ManyToManyField(to='library.Quality')),
            ],
        ),
        migrations.CreateModel(
            name='StreamTmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmppath', models.CharField(max_length=255)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Stream')),
            ],
        ),
    ]
