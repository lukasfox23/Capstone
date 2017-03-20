from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from basic.models import Conference,UserConference,Item,Comment
from django.contrib.auth.decorators import login_required
from capstone.forms import ConferenceForm,FileForm
# Create your views here.
# Thinking this url should look something like /basic/conference/"conference name"
def conference(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # Hardcoded to add to conference 1 rn, need to change
            newFile = Item(user_id = User.objects.get(username = request.user), conference_id = Conference.objects.get(conference_id = 1),file_path = request.FILES['file_path'])
            newFile.save()

            return render(request, "conference/conference.html")
    else:
        form = FileForm()
    return render(request, "conference/conference.html", {'form':form})

def createconference(request):
    if request.method == "POST":
        form = ConferenceForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            new_conference=Conference.objects.create(conference_name=data['conference_name'],conference_info=data['conference_info'],conference_address=data['conference_address'],conference_city=data['conference_city'],conference_state=data['conference_state'],attendee_count=1,available_count=data['available_count'])
            if(new_conference):
                new_conference.save()
            return render(request, "conference/conference.html", {'data':data})
    else:
        form = ConferenceForm()
    return render(request, 'conference/createconference.html', {'form':form})

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
