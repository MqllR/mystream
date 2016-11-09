#!/usr/bin/python

from django import forms

from .models import Category, Quality
from .models import LANGUAGE_CHOICE

class StreamForm(forms.Form):

    stream_name = forms.CharField(label='Name', max_length=100)
    stream_description = forms.CharField(label='Description', widget=forms.Textarea)
    stream_quality = forms.ModelMultipleChoiceField(
                                queryset=Quality.objects.all(),
                                widget=forms.CheckboxSelectMultiple,
                        )
    stream_language =  forms.ChoiceField(choices=LANGUAGE_CHOICE)
    stream_category = forms.ModelChoiceField(queryset=Category.objects.all())
