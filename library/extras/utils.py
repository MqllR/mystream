#!/usr/bin/python

import os

from django.conf import settings

def handle_uploaded_file(f):
    
    path_name = settings.MEDIA_TMP + '/.' + f.name

    if not os.path.exists(path_name):
        with open(path_name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        return True

    else:
        return False
