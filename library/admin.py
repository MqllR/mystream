from django.http.response import HttpResponseRedirect
from django import forms
from django.contrib import admin
from models import *

import os
from mystream.settings import *
from library.extras.encode import Encode
from pprint import pprint

# Register your models here.

class StreamAdmin(admin.ModelAdmin):
    exclude = [ 'encoded' ]

    def save_model(self, request, obj, form, change):
        """ Here we can encode video to ogg format and deplace to the rigth place """

        if not change:
            obj.save()

            # start a thread, pass obj to extras class, encode and update DB
            thread = Encode(obj)
            thread.start()
            print('in main')

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect('/library/encoding_process')

admin.site.register(Stream, StreamAdmin)
admin.site.register(Category)
