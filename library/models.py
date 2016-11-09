#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Quality(models.Model):
    
    name = models.CharField(max_length=15)
    cmd = models.CharField(max_length=255)
    directory = models.CharField(max_length=20)

    def __str__(self):
        return self.name

LANGUAGE_CHOICE = (
    ('VF', 'VF'),
    ('VOSTFR', 'VOSTFR'),
    ('VO', 'VO'),
)

class Stream(models.Model):
    
    name = models.CharField(
                max_length=60,
            )

    description = models.TextField()
    
    quality = models.ManyToManyField(Quality)

    movie = models.CharField(
                max_length=255,
                null=True,
            )

    encoded = models.BooleanField(default=0)
    
    date = models.DateTimeField(auto_now=True)

    language = models.CharField(
                max_length=10, 
                choices=LANGUAGE_CHOICE, 
                default='VOSTFR',
            )

    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

class StreamTmp(models.Model):

    tmppath = models.CharField(
                max_length=255,
            )

    stream = models.ForeignKey(Stream)
