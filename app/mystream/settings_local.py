#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .settings import BASE_DIR

ALLOWED_HOSTS = [
        '127.0.0.1',
        '5.196.17.86',
]

# DB parameters
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        #'USER': 'ansibleapi',
        #'PASSWORD': 'mypassword',
        #'HOST': 'localhost',
        #'PORT': '3306',
    }
}

MEDIA_TMP = '/media/tmp'
MEDIA_URL = '/media/stream/'

# Static file to be collected
STATIC_ROOT = '/static'

# Where to store TemporaryUploadedFile
FILE_UPLOAD_TEMP_DIR = BASE_DIR + MEDIA_TMP
