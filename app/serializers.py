from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resolutions
        fields = '__all__'