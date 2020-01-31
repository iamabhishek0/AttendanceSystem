from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action
from .serializer import LocationSerializer
from .models import Location


class test(APIView):
    # def get(self,request):
        
    #     location = Location.objects.all()
    #     serializer = LocationSerializer(location, many=True)
    #     return Response({"location": serializer})
    def post(self,request):
        print(request.data.get('location'))
        Location.objects.create(
            location_coordinates=request.data.get('location'))
        return Response({'work':'sexy'})