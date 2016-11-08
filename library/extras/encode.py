#!/usr/bin/python

import re
import os

from subprocess import call

from django.conf import settings

from library.models import Stream, StreamTmp, Quality
from .utils import check_extension

CMD_FFMEG                   = '/usr/bin/ffmpeg'


class Encode():
    """
    Take a src file in param and a queryset of quality before process encoding.

    This class is executed by Celery instance.
    """
    
    
    def __init__(self, streamtmp, quality='low'):

        if not os.path.exists(CMD_FFMEG):
            raise Exception('ffmpeg binarie is not available')

        try:
            StreamTmp.objects.get(tmppath=streamtmp)
            self.streamtmp = streamtmp
        except Exception as e:
            print("Error : %s" % str(e))

        try:
            self.quality = Quality.objects.get(name=quality)
        except Exception as e:
            print("Error : %s" % str(e))


    def _set_filename(self):
        """
        Build stream name
        """

        self.stream = Stream.objects.get(streamtmp__tmppath=self.streamtmp)

        self.stream_name = self.stream.name.lower().replace(' ', '_') + '.mp4'

    def _pre_encoding(self):
        """
        Execute before running process encoding
        """

        if not os.path.exists(settings.BASE_DIR + settings.MEDIA_URL + self.quality.directory):
            try:
                os.mkdir(settings.BASE_DIR + settings.MEDIA_URL + self.quality.directory, 0755)
            except Exception as e:
                print('Error mkdir : %s' % str(e))

        if os.path.exists(settings.BASE_DIR + settings.MEDIA_URL + self.quality.directory + self.stream_name):
            try:
                os.remove(settings.BASE_DIR + settings.MEDIA_URL + self.quality.directory + self.stream_name)
            except Exception as e:
                print('Error remove : %s' % str(e))


    def post_encoding(self):
        """
        Execute after process encoding by celery chord
        """

        try:
            os.remove(self.streamtmp)
            
            stream = Stream.objects.get(streamtmp__tmppath=self.streamtmp)
            stream.encoded = 1
            stream.save()

            StreamTmp.objects.get(tmppath=self.streamtmp).delete()
        except Exception as e:
            print("Error remove : %s" % str(e))


    def run(self):
        """
        Run process encoding
        """

        self._set_filename()

        try:
            self._pre_encoding()

            retcode = call(CMD_FFMEG + ' ' + self.quality.cmd \
                                % (self.streamtmp, settings.BASE_DIR + settings.MEDIA_URL + self.quality.directory + self.stream_name), shell=True)

        except Exception as e:
            print("Error encoding : %s" % str(e))
