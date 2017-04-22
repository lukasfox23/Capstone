from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from basic.models import Conference,UserConference,Item,Comment
from django.contrib.auth.decorators import login_required
from capstone.forms import ConferenceForm,FileForm,EditConferenceForm
from django.contrib import messages
# Create your views here.
# Thinking this url should look something like /basic/conference/"conference name"
def conference(request, conference_id):
    confId = conference_id
    desiredConf = Conference.objects.filter(conference_id = confId)
    items = Item.objects.filter(conference_id = confId)
    # Use desiredConf[0] to access what should be the only conference in this variable
    # Method for uploading papers, should move to model for cleanliness
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        editForm = EditConferenceForm()
        # Edit the event and render the page again
        if request.POST.get("editSubmit"):
            editEvent(request, desiredConf, items, form)

        # Add a new file to the event
        if form.is_valid():
            newFile = Item(user_id = User.objects.get(username = request.user),
                                                      conference_id = Conference.objects.get(conference_id = desiredConf[0].conference_id),
                                                      file_path = request.FILES['file_path'])
            newFile.save()
            return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form, 'confItems':items, 'editForm':editForm})
        if request.POST.get("attendSubmit"):
            if UserConference.checkUnique(User.objects.get(username = request.user), Conference.objects.get(conference_id = desiredConf[0].conference_id)):
                newConferenceAttendee = UserConference(user_id = User.objects.get(username = request.user), conference_id = Conference.objects.get(conference_id = desiredConf[0].conference_id), user_type = "G")
                newConferenceAttendee.save()
                messages.add_message(request, messages.SUCCESS, "You are now attending this conference!")
            else:
                messages.add_message(request, messages.ERROR, "You are already attending this conference!")
            return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form})
    else:
        form = FileForm()
        editForm = EditConferenceForm()
    return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form, 'confItems':items, 'editForm':editForm})

# Method for editing events
def editEvent(request, desiredConf, items, form):
    editForm = EditConferenceForm(request.POST)

    if editForm.is_valid():
        editData = editForm.cleaned_data

        if editData['conference_info'] is not None:
            Conference.objects.filter(conference_id = desiredConf[0].conference_id).update(conference_info = editData['conference_info'])

        if editData['conference_address'] is not None:
            Conference.objects.filter(conference_id = desiredConf[0].conference_id).update(conference_address = editData['conference_address'])

        if editData['conference_city'] is not None:
            Conference.objects.filter(conference_id = desiredConf[0].conference_id).update(conference_city = editData['conference_city'])

        if editData['conference_state'] is not None:
            Conference.objects.filter(conference_id = desiredConf[0].conference_id).update(conference_state = editData['conference_state'])

    return render(request, "conference/conference.html", {'desiredConf':desiredConf[0], 'form':form, 'confItems':items, 'editForm':editForm})


#def createconference(request):
#    if request.method == "POST":
#        form = ConferenceForm(request.POST)
#        if form.is_valid():
#            data = form.cleaned_data
#            new_conference = Conference.objects.create(conference_name=data['name'],conference_info=data['info'],conference_address=data['address'],conference_city=data['city'],conference_state=data['state'],attendee_count=1,available_count=data['available'])
#            if(new_conference):
#                new_conference.save()
#                # Make the person who created the conference an admin of that conference
#                CreateConferenceAdmin = UserConference.objects.create(user_id = User.objects.get(username = request.user), conference_id = new_conference, user_type = "A")
#                CreateConferenceAdmin.save()
#            return conference(request, new_conference.conference_id)
#    else:
#        form = ConferenceForm()
#        return render(request, 'conference/createconference.html', {'form':form})

# Gets and displays a list of currently available conferences
def gallery(request):
    currentUser = request.user
    Conferences = Conference.objects.all()
    form = ConferenceForm()

    # The user attempts to create an event
    if request.method == "POST":
        form = ConferenceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_conference = Conference.objects.create(conference_name=data['name'],
                                                       conference_info=data['info'],
                                                       conference_address=data['address'],
                                                       conference_city=data['city'],
                                                       conference_state=data['state'],
                                                       attendee_count=1,
                                                       available_count=data['available'])

            if(new_conference):
                new_conference.save()
                # Make the person who created the conference an admin of that conference
                CreateConferenceAdmin = UserConference.objects.create(user_id = User.objects.get(username = request.user), conference_id = new_conference, user_type = "A")
                CreateConferenceAdmin.save()
            return conference(request, new_conference.conference_id)

    # The user enters a name search
    elif request.method == "GET":
        # Get the search result
        search = request.GET.get('conferenceNameSearch')
        # Verify there's something there
        if search is not None:
            # Get list of conferences with name like input
            Conferences = Conference.objects.filter(conference_name__contains = search)
            form = ConferenceForm()
        else:
            Conferences = Conference.objects.all()
            form = ConferenceForm()
        return render(request, "conference/gallery.html", {'Conferences':Conferences, 'form':form})

    else:
        Conferences = Conference.objects.all()
        form = ConferenceForm()
    return render(request, "conference/gallery.html", {'Conferences':Conferences, 'form':form})

@login_required(login_url='login/')
def account(request):
    CurrentUser = request.user
    conference_list = UserConference.objects.filter(user_id = CurrentUser.id)
    item_list = Item.objects.filter(user_id = CurrentUser.id)
    if(conference_list):
        Conferences = Conference.objects.filter(conference_id__in=conference_list.values('conference_id'))
    else:
        Conferences = ''

    if(item_list):
        Items = Item.objects.filter(item_id__in = item_list.values('item_id'))
    else:
        Items = ''
    return render(request, "conference/account.html",{'Conferences':Conferences, 'Items':Items})

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
