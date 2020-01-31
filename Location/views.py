from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class GetPostLocation(APIView):

    def post(self, request, format=None):
        
        user = request.P

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)