from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
        model = User
        fields = "__all__"

class FarmerSerializer(serializers.ModelSerializer):
      class Meta:
        model = Farmer
        fields = "__all__"

class AgriInfoSerializer(serializers.ModelSerializer):
      class Meta:
        model = AgriInfo
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
      class Meta:
        model = ProductCategory
        fields = "__all__"