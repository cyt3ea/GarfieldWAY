from django import forms
from django.forms import Textarea
from .models import Pin
from django import forms
from django.forms import Textarea
from .models import Pin
from django.db import models
from django.contrib.admin import widgets


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('pub_date',)
        labels = {
            'pin_name': 'Name ',
            'pin_room': 'Room ',
            'other_pin_room': 'Other Room ',
            'pin_description': 'Description',
            'pin_type': 'Type',
            'date': 'Date',
            'votes':'Up Votes'
        }
        help_texts = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'pin_room': '100-124 or 200-240 or 300-340 (Optional)',
            'other_pin_room': 'e.g. Gym, Commons, Field (Optional)',
        }
        widgets = {
            'pin_description': Textarea(),
        }
