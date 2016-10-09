#!/usr/bin/python

import re

from os import system
from threading import Thread, RLock

from django.conf import settings

# To serialize encoding process
lock = RLock()

RE_STREAM_AVI_EXT = re.compile(r'^.*/\.(?P<stream_name>.*)\.avi$')

class Encode(Thread):
    
    def __init__(self, file_path):
        super(Encode, self).__init__()
        self.file_path_src = file_path
        #self.obj = obj

    def run(self):
        with lock:
            self._convert_avi_mp4()
            

    def _convert_avi_mp4(self):
        if RE_STREAM_AVI_EXT.match(self.file_path):
            self.file_path_dst = settings.MEDIA_STREAM + '/' + re.group('stream_name') + '.mp4'

            try:
                os.system("ffmpeg -i %s -c:v libx264 -pix_fmt yuv420p -movflags faststart %s" \
                                    % (self.file_path_src, self.obj))
            except:
                pass
