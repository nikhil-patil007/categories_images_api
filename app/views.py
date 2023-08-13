from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *

# Create your views here.

@api_view(["GET"])
def home_page_api(request):
    '''
     API For the Home Page to displayed the all images and Files.
    '''
    recommended_image = DataStorage.objects.filter(Recommended="Yes")
    List_of_image = []
    for arr in recommended_image:
        array_object = {}
        array_object['id'] = arr.id
        array_object['type_of'] = arr.type_of
        array_object['parent_category'] = arr.parent_category.name
        array_object['File'] = arr.file_url
        array_object['Recommended'] = arr.Recommended
        List_of_image.append(array_object)
        
    return Response({'status':1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def Main_category_api(request):
    '''
    API for the getting List of main category.
    '''
    allCategories = Categories.objects.get(parent_category=None)
    return Response({'status':1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)