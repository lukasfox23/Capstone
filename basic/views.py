from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from basic.models import Conference,UserConference,Item,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from capstone.forms import UserForm
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
# This function will return the Login page for the user to attempt to log in.
def login(request):
    return render(request, "basic/login.html")

# This function handles
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # new_user = User.objects.create_user(**form.cleaned_data)
            new_user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
            new_user = authenticate(username=data['username'], password=data['password'])
            if new_user:
                auth_login(request, new_user)
            return render(request, "basic/basic.html")
    else:
        form = UserForm()
        return render(request,'basic/register.html', {'form':form})

#@login_required(login_url='login/')
def index(request):
    # Get conferences to populate main page slider. TODO Add date field & only display upcoming conferences
    Conferences = Conference.objects.all()
    return render(request, "basic/basic.html",{'Conferences': Conferences})

def page_not_found(request):
    response = render_to_response(
    '404.html',
    context_instance=RequestContext(request)
    )

    response.status_code = 404
    return response

def page_denied(request):
    response = render_to_response(
    '403.html',
    context_instance=RequestContext(request)
    )

    response.status_code = 403
    return response

def bad_request(request):
    response = render_to_response(
    '400.html',
    context_instance=RequestContext(request)
    )

    response.status_code = 400
    return response
