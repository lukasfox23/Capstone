from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from basic.models import Conference,UserConference,Item,Comment
from django import forms
from datetime import datetime

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type':'password'}))

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

# For uploading papers/covers etc
class FileForm(forms.Form):
    file_path = forms.FileField(
        label = 'Select a file',
        help_text = 'Only pdfs accepted'
    )

class ConferenceForm(forms.Form):
    name = forms.CharField(max_length=75)
    info = forms.CharField(widget=forms.Textarea)
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=20)
    start = forms.DateTimeField()
    end = forms.DateTimeField()
    available = forms.IntegerField()
