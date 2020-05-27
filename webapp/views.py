from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import json
from django.http import JsonResponse

# Create your views here.

class userList(APIView):
    def get(self, request):
        
        users = User.objects.all().values() #Returns all feilds
        users_list = list(users)  
        for user in users_list:
            print(user)
        return JsonResponse(users_list, safe=False)
        
  
class userListUI(APIView): #For viewing data in APIview
    def get(self, request):
        
        abl1 = User.objects.all()
        sls = UserSerializer(abl1, many = True)
        return Response(sls.data)
        

