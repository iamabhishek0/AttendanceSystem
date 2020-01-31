from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField()
    

class AttendanceTable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location_verified = models.NullBooleanField()
    voice_verified = models.NullBooleanField()
    face_verified = models.NullBooleanField()

class Centers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    center_id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
