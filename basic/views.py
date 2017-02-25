from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
# Create your views here.
# This function will return the Login page for the user to attempt to log in.
def login(request):
    return render(request, "basic/login.html")

def register(request):
    return render(request, "basic/register.html")

#@login_required(login_url='login/')
def index(request):
    return render(request, "basic/basic.html")

def gallery(request):
    return render(request, "basic/gallery.html")

# Thinking this url should look something like /basic/conference/"conference name"
def conference(request):
    return render(request, "basic/conference.html")

#@login_required(login_url='login/')
def account(request):
    return render(request, "basic/account.html")

#@login_required(login_url='login/')
def myPapers(request):
    return render(request, "basic/mypapers.html")

#@login_required(login_url='login/')
def myConferences(request):
    return render(request, "basic/myconferences.html")
