#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import StreamListView, StreamDetailView, StreamViewDetailView

urlpatterns = [
    url(r'(?P<category>movie|serie)/', StreamListView.as_view(), name='stream'),
    url(r'stream/(?P<stream_id>\d+)/', StreamDetailView.as_view(), name='stream_id'),
    url(r'stream/view/(?P<stream_id>\d+)/', StreamViewDetailView.as_view(), name='stream_view'),
    url(r'$', StreamListView.as_view(), name='index_library'),
]
