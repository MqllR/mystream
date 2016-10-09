#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView
from .views import upload_file

urlpatterns = [
    url(r'encoding_process', TemplateView.as_view(template_name='encoding_process.html')),
    url(r'error', TemplateView.as_view(template_name='error.html')),
    url(r'upload', upload_file),
]
