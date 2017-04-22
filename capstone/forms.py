from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from basic.models import Conference,UserConference,Item,Comment
from django import forms
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type':'password'}))

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'name': 'email', 'type': 'email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password'})
        }
        labels = {
            'username': _('Username:'),
            'email': _('Email:'),
            'password': _('Password:')
        }

# For uploading papers/covers etc
class FileForm(forms.Form):
    file_path = forms.FileField(
        label = 'Select a file',
        help_text = 'Only pdfs accepted'
    )

class EditConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = ('conference_info',
                  'conference_address',
                  'conference_city',
                  'conference_state')
        widgets = {
            'conference_info': forms.TextInput(attrs={'class': 'form-control', 'name': 'info'}),
            'conference_address': forms.TextInput(attrs={'class': 'form-control', 'name': 'address'}),
            'conference_city': forms.TextInput(attrs={'class': 'form-control', 'name': 'city'}),
            'conference_state': forms.TextInput(attrs={'class': 'form-control', 'name': 'state'})
        }
        labels = {
            'conference_info': _('Info:'),
            'conference_address': _('Street Address:'),
            'conference_city': _('City:'),
            'conference_state': _('State:')
        }

class ConferenceForm(forms.Form):
    name = forms.CharField(label="Event Name:", max_length=75,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'name'}))
    info = forms.CharField(label="Event Info:",
                           widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'info'}))
    address = forms.CharField(label="Street Address:", max_length=50,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'address'}))
    city = forms.CharField(label="City:", max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'city'}))
    state = forms.CharField(label="State:", max_length=20,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'state'}))
    #start = forms.DateTimeField()
    #end = forms.DateTimeField()
    available = forms.IntegerField(label="How many people can come?:",
                                   widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'available'}))
