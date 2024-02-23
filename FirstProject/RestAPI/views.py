from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import userRegister
from .serializers import userRegisterSerializer


@api_view(["GET"])
def getUserDetails(request):
   user =  userRegister.objects.all()
   serializers = userRegisterSerializer(user , many=True)
   return Response(serializers.data)

@api_view(["POST"])
def createuser(request):
   newuser  = userRegisterSerializer(data=request.data)
   if newuser.is_valid():
      newuser.save()
   return  Response(newuser.data)
