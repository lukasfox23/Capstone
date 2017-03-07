from django.contrib import admin
from basic.models import Conference,UserConference,Item,Comment

# Register your models here.
admin.site.register(Conference)
admin.site.register(UserConference)
admin.site.register(Item)
admin.site.register(Comment)