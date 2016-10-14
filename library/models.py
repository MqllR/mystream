#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Stream(models.Model):
    
    name = models.CharField(
                max_length=60,
            )

    description = models.TextField()

    movie = models.CharField(
                max_length=255,
                null=True,
            )

    encoded = models.BooleanField(default=1)

    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

class StreamTmp(models.Model):

    tmppath = models.CharField(
                max_length=255,
            )

    stream = models.ForeignKey(Stream)
