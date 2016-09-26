#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'encoding_process', TemplateView.as_view(template_name='encoding_process.html')),
]
