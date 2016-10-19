#!/usr/bin/python

import re
import os

from subprocess import call

from django.conf import settings

from library.models import Stream, StreamTmp
from .utils import check_extension

CMD_FFMEG                   = '/usr/bin/ffmpeg'
CMD_CONVERT_AVI_TO_MP4      = CMD_FFMEG + " -i %s -c:v libx264 -pix_fmt yuv420p -movflags faststart %s"

class Encode():
    
    def __init__(self, streamtmp):

        if not os.path.exists(CMD_FFMEG):
            raise Exception('ffmpeg binarie is not available')

        try:
            StreamTmp.objects.get(tmppath=streamtmp)
            self.streamtmp = streamtmp
        except Exception as e:
            print("Error : %s" % str(e))

    def _set_filename(self):
        self.stream = Stream.objects.get(streamtmp__tmppath=self.streamtmp)

        self.stream_name = self.stream.name.lower().replace(' ', '_') + '.mp4'

    def _pre_encoding(self):
        if os.path.exists(settings.BASE_DIR + settings.MEDIA_URL + self.stream_name):
            try:
                os.remove(settings.BASE_DIR + settings.MEDIA_URL + self.stream_name)
            except Exception as e:
                print('Error remove : %s' % str(e))

    def _post_encoding(self):
        try:
            os.remove(self.streamtmp)
            
            self.stream.movie = self.stream_name
            self.stream.encoded = 1
            self.stream.save()

            StreamTmp.objects.get(tmppath=self.streamtmp).delete()
        except Exception as e:
            print("Error remove : %s" % str(e))

    def run(self):
        self._set_filename()

        try:
            self._pre_encoding()

            retcode = call(CMD_CONVERT_AVI_TO_MP4 \
                                % (self.streamtmp, settings.BASE_DIR + settings.MEDIA_URL + self.stream_name), shell=True)

            self._post_encoding()
        except Exception as e:
            print("Error encoding : %s" % str(e))

