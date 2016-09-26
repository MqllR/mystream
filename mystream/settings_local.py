#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

MEDIA_ROOT = '/home/mql/dev/python/mystream/media'

MEDIA_TMP = MEDIA_ROOT + '/tmp'
MEDIA_STREAM = MEDIA_ROOT + '/stream'
