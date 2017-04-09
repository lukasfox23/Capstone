from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from basic.models import Conference,UserConference,Item,Comment
from django.contrib.auth.decorators import login_required
from capstone.forms import ConferenceForm,FileForm
# Create your views here.
# Thinking this url should look something like /basic/conference/"conference name"
def conference(request, conference_id):
    confId = conference_id
    desiredConf = Conference.objects.filter(conference_id = confId)
    # Use desiredConf[0] to access what should be the only conference in this variable
    # Method for uploading papers, should move to model for cleanliness
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newFile = Item(user_id = User.objects.get(username = request.user), conference_id = Conference.objects.get(conference_id = desiredConf[0].conference_id),file_path = request.FILES['file_path'])
            newFile.save()

            return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form})
        print request.POST
        if request.POST.get("attendSubmit"):
            newConferenceAttendee = UserConference(user_id = User.objects.get(username = request.user), conference_id = Conference.objects.get(conference_id = desiredConf[0].conference_id), user_type = "G")
            newConferenceAttendee.save()
            return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form})
    else:
        form = FileForm()
    return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form})

def createconference(request):
    if request.method == "POST":
        form = ConferenceForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            new_conference=Conference.objects.create(conference_name=data['conference_name'],conference_info=data['conference_info'],conference_address=data['conference_address'],conference_city=data['conference_city'],conference_state=data['conference_state'],attendee_count=1,available_count=data['available_count'])
            if(new_conference):
                new_conference.save()
            # Not navigating to the proper url
            #return render(request, "conference/conference.html", {'newConference':new_conference.conference_id,'data':data})
            return conference(request, new_conference.conference_id)
    else:
        form = ConferenceForm()
    return render(request, 'conference/createconference.html', {'form':form})

# Gets and displays a list of currently available conferences
def gallery(request):
    currentUser = request.user
    # The user enters a name search
    if request.method == "GET":
        # Get the search result
        search = request.GET.get('conferenceNameSearch')
        # Verify there's something there
        if search is not None:
            # Get list of conferences with name like input
            Conferences = Conference.objects.filter(conference_name__contains = search)
        else:
            Conferences = Conference.objects.all()
        return render(request, "conference/gallery.html", {'Conferences':Conferences})
    else:
        Conferences = Conference.objects.all()
    return render(request, "conference/gallery.html", {'Conferences':Conferences})

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
