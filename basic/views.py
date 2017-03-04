from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.template import RequestContext
from capstone.forms import RegistrationForm
# Create your views here.
# This function will return the Login page for the user to attempt to log in.
def login(request):
    return render(request, "basic/login.html")

# This function handles
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data['username'],password=data['password'],email=data['email'])
            new_user = authenticate(username=data['username'],password=data['password'])
            if new_user:
                auth_login(request, new_user)
                userInfo.save()
            return render(request, "basic/basic.html")
    else:
        form = RegistrationForm()
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

#These last two probably don't need to be pages
#@login_required(login_url='login/')
def myPapers(request):
    return render(request, "basic/mypapers.html")

#@login_required(login_url='login/')
def myConferences(request):
    return render(request, "basic/myconferences.html")

def ContentView(request):
    return render(request, "basic/contentview.html")
