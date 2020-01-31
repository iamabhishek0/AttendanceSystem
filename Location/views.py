from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action
from .serializer import LocataionSerializer
from .models import Location


class test(APIView):
    def get(self,request):
        todo=Todo.objects.all()
        serializer=TodoSerializer(todo,many=True)
        return Response(serializer.data)
    def post(self,request):
        Todo.objects.create(
            title=request.POST.get('title'),
            text=request.POST.get('text'))
        return HttpResponse(status=201)