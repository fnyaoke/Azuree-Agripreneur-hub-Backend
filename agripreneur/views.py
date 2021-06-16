from django.shortcuts import render
from django.core.checks import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

# Create views
class Registration(APIView):
        serializer_class=RegistrationSerializer

        def post(self, request):
            serializer=self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            user_data=serializer.data

            response={
                "data":{
                    "user":dict(user_data),
                    "status":"Success",
                    "message":"User account created successfully"
                }

            }
            return Response(response, status=status.HTTP_201_CREATED)

        def get(self,request,format=None):
            users= User.objects.all()
            serializers=RegistrationSerializer(users, many=True)
            return Response(serializers.data)

class LoginUser(APIView):
    serializer_class=LoginSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    # login user
    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            users=serializers.data

            response={
                "data":{
                    "new_hood":dict(users),
                    "status":"Success",
                    "message":"User logged in successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# list views

class UserList(APIView):
  def get_users(self, pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Http404()

  def get(self,request, format=None):
    user= User.objects.all()
    serializers=ProfileSerializer(user, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=ProfileSerializer(data=request.data)
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
    serializers = ProfileSerializer(user, request.data)
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
class UserDetails(APIView):
    # get a specific user's details
    def get_users(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user=self.get_users(pk)
        serializers=ProfileSerializer(user)
        return Response(serializers.data)

    # update an existing user
    def put(self, request, pk, format=None):
        user=self.get_users(pk)
        serializers=ProfileSerializer(user, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete an existing user
    def delete(self, request, pk, format=None):
        user=self.get_users(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AgriInfo(APIView):
  def get_agriInfo(self, pk):
    try:
        return AgriInfo.objects.get(pk=pk)
    except AgriInfo.DoesNotExist:
        return Http404()

  def get(self,request, format=None):
    agriInfo= AgriInfo.objects.all()
    serializers=AgriInfoSerializer(agriInfo, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=AgriInfoSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      agriInfo=serializers.data
      response = {
          'data': {
              'user': dict(agriInfo),
              'status': 'success',
              'message': "Information added successfully"
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)


  def put(self, request, pk, format=None):
    agriInfo = self.get_agriInfo(pk=pk)
    serializers = AgriInfoSerializer(agriInfo, request.data)
    if serializers.is_valid():
      serializers.save()
      user=serializers.data
      response = {
          'data': {
              'user': dict(agriInfo),
              'status': 'success',
              'message': "Information updated successfully"
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    agriInfo = self.get_agriInfo(pk=pk)
    agriInfo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


