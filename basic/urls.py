from django.conf.urls import url,handler404,handler403,handler400
from . import views

handler404 = 'capstone.views.page_not_found'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
]
