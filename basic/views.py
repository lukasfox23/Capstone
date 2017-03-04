from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from capstone.forms import UserForm
# Create your views here.
# This function will return the Login page for the user to attempt to log in.
def login(request):
    return render(request, "basic/login.html")

# This function handles
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            if new_user:
                auth_login(request, new_user)
            return render(request, "basic/basic.html")
    else:
        form = UserForm()
        return render(request,'basic/register.html', {'form':form})

#@login_required(login_url='login/')
def index(request):
    return render(request, "basic/basic.html")

def gallery(request):
    return render(request, "basic/gallery.html")

#@login_required(login_url='login/')
def account(request):
    return render(request, "basic/account.html")

#These last two probably don't need to be pages
#@login_required(login_url='login/')
def myPapers(request):
    return render(request, "basic/mypapers.html")

#@login_required(login_url='login/')

def ContentView(request):
    return render(request, "basic/contentview.html")
