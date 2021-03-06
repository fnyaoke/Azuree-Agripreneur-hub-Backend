from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django import forms

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
        model = Profile
        exclude= ["name"]


class AgriInfoSerializer(serializers.ModelSerializer):
      class Meta:
        model = AgriInfo
        fields = "__all__"
class MarketSerializer(serializers.ModelSerializer):
      class Meta:
        model = Market
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
      email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
      password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
      class Meta:
            model = User
            fields = ['username','email','password', 'password2']
            extra_kwargs = {
            "password": {'write_only': True}
            }

      def save(self):
            user = User(
                    username = self.validated_data['username'],
                    email = self.validated_data['email'],
                )
            password = self.validated_data['password']
            password2 = self.validated_data['password2']

            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match'})

            user.set_password(password)
            user.save()
            return user

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }

    )
    class Meta:
        model=User
        fields=["username", "password"]