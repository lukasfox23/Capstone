from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
# Thinking this url should look something like /basic/conference/"conference name"
def conference(request):
    return render(request, "conference/conference.html")

def gallery(request):
    return render(request, "conference/gallery.html")

#@login_required(login_url='login/')
def account(request):
    return render(request, "conference/account.html")

#These last two probably don't need to be pages
#@login_required(login_url='login/')
def myPapers(request):
    return render(request, "conference/mypapers.html")

#@login_required(login_url='login/')

def ContentView(request):
    return render(request, "conference/contentview.html")

#@login_required(login_url='login/')
def myConferences(request):
    return render(request, "conference/myconferences.html")