from rest_framework import serializers
from .models import Location

class LocataionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("location_coordinates")