from django.conf.urls import url,handler404,handler403,handler400
from . import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'capstone.views.page_not_found'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
]

if settings.DEBUG is True:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
