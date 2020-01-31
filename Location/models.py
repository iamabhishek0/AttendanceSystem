from django.db import models

class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location_coordinates = models.DecimalField()
    
