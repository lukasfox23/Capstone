from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^conference/$', views.conference, name='conference'),
    url(r'^account/$', views.account, name='account'),
    url(r'^mypapers/$', views.myPapers, name='mypapers'),
    url(r'^myconferences/$', views.myConferences, name='myconferences'),
    url(r'^contentview/$', views.ContentView, name='contentview'),
]
