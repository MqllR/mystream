#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location = '/tmp/')

class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Stream(models.Model):
    
    name = models.CharField(
                max_length=30,
                default=None
            )

    description = models.TextField(default=None)

    movie = models.FileField(
                upload_to='tmp/',
                storage=fs
            )

    encoded = models.BooleanField(default=False)

    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
