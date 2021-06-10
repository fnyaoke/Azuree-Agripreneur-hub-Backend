from django.shortcuts import render
from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import UserSerializer,AgriInfoSerializer,ProductCategorySerializer,FarmerSerializer


# list views

class UserList(APIView):
  def get_users(self, pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Http404()

  def get(self,request, format=None):
    user= User.objects.all()
    serializers=UserSerializer(user, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=UserSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      user=serializers.data
      response = {
          'data': {
              'user': dict(user),
              'status': 'success',
              'message': "User created successfully"
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)


  def put(self, request, pk, format=None):
    user = self.get_users(pk=pk)
    serializers = UserSerializer(user, request.data)
    if serializers.is_valid():
      serializers.save()
      user=serializers.data
      response = {
          'data': {
              'user': dict(user),
              'status': 'success',
              'message': "user updated successfully"
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    user = self.get_users(pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
