#!/usr/bin/python

from django import forms

class StreamForm(forms.Form):

    stream_name = forms.CharField(label='Name', max_length=100)
    stream_description = forms.CharField(label='Description', widget=forms.Textarea)
    stream_file = forms.FileField(label='File')
