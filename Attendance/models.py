from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
    FCMid = models.CharField()

class AttendanceTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.OneToOneField("Attendance.Attendance", on_delete=models.CASCADE)
    location_verified = models.NullBooleanField()
    voice_verified = models.NullBooleanField()
    face_verified = models.NullBooleanField()