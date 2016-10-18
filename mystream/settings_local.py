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

MEDIA_ROOT = '/home/mael/dev/mystream/media'

MEDIA_TMP = MEDIA_ROOT + '/tmp'
MEDIA_STREAM = MEDIA_ROOT + '/stream'

# Where to store TemporaryUploadedFile
FILE_UPLOAD_TEMP_DIR = MEDIA_TMP


#import djcelery
#djcelery.setup_loader()

BROKER_URL = 'django://'
