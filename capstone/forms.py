from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from basic.models import Conference,UserConference,Item,Comment
from django import forms

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

class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = ['conference_name','conference_info','conference_address','conference_city','conference_state','available_count']
