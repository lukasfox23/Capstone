from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^conference/$', views.conference, name='conference'),
]