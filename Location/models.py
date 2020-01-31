from django.db import models

class Location(models.Model):
    location_coordinates = models.IntegerField()
    
