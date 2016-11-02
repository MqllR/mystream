#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import StreamListView, StreamDetailView, StreamViewDetailView, StreamSearchListView

urlpatterns = [
    url(r'search/', StreamSearchListView.as_view(), name='search'),
    url(r'cat/(?P<category>\w+)/', StreamListView.as_view(), name='stream_cat'),
    url(r'stream/(?P<stream_id>\d+)/', StreamDetailView.as_view(), name='stream_id'),
    url(r'stream/view/(?P<stream_id>\d+)/', StreamViewDetailView.as_view(), name='stream_view'),
]
