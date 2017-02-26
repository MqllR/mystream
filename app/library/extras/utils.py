#!/usr/bin/python

import os
import re

from django.conf import settings

# EXTENSION
RE_AVI_EXTENSION    = re.compile(r'^.*\.avi$')

def check_extension(streamname):
    if re.match(RE_AVI_EXTENSION, streamname):
        return 'avi'

