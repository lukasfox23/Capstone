from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^conference/$', views.conference, name='conference'),
    #url(r'^createconference/$', views.createconference, name='createconference'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^(?P<conference_id>[0-9]+)/$', views.conference, name='conference'),
    url(r'^account/$', views.account, name='account'),
    url(r'^mypapers/$', views.myPapers, name='mypapers'),
    url(r'^myconferences/$', views.myConferences, name='myconferences'),
    url(r'^(?P<conference_id>[0-9]+)/(?P<item_id>[0-9]+)/$', views.ContentView, name='contentview'),
]
