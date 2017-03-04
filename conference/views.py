from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
# Thinking this url should look something like /basic/conference/"conference name"
def conference(request):
    return render(request, "conference/conference.html")