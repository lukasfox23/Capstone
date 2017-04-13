from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Conference(models.Model):
    conference_id = models.AutoField(primary_key=True)
    conference_name = models.CharField(max_length=75)
    conference_info = models.TextField()
    conference_address = models.CharField(max_length=50)
    conference_city = models.CharField(max_length=20)
    conference_state = models.CharField(max_length=20)
    conference_start = models.DateTimeField(default=datetime.now)
    conference_end = models.DateTimeField(default=datetime.now)
    attendee_count = models.IntegerField()
    available_count = models.IntegerField()
    header_path = models.FileField(upload_to='headers/')

class UserConference(models.Model):
    USER_TYPES = (
        ('A','Admin'),
        ('R','Reviewer'),
        ('G', 'Guest'),
        ('S', 'Submitter')
    )
    user_id = models.ForeignKey(User)
    conference_id = models.ForeignKey(Conference)
    user_type = models.CharField(max_length=1, choices=USER_TYPES)

    @classmethod
    def checkUnique(conference, uid, cid):
        try:
            conference.objects.get(user_id = uid, conference_id = cid)
            return False
        except:
            return True

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    conference_id = models.ForeignKey(Conference)
    file_path = models.FileField(upload_to='uploads/')
    approval_flag = models.BooleanField(default=False)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item)
    comment = models.CharField(max_length=120)
