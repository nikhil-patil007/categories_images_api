from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

def List_for_data_store(values):
    List_of_data = list()
    for arr in values:
        array_object = dict()
        array_object["id"] = arr.id
        array_object["type_of"] = arr.type_of
        array_object["parent_category"] = arr.parent_category.name
        array_object["File"] = arr.file_url
        array_object["Recommended"] = arr.Recommended
        List_of_data.append(array_object)

    return List_of_data

@api_view(["GET"])
def home_page_api(request):
    '''
     API For the Home Page to displayed the all images and Files.
    '''
    recommended_image = DataStorage.objects.filter(Recommended="Yes")
    List_of_image = List_for_data_store(recommended_image)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def Get_all_resolutions(request):
    '''
    Get the List of All Resolutions
    '''
    getAllResolutions = Resolutions.objects.all()
    List_of_resolutions = ResolutionSerializer(getAllResolutions,many=True)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_resolutions.data} ,status=status.HTTP_200_OK)

@api_view(["GET"])
def Main_category_api(request):
    '''
    API for the getting List of main category.
    if Param_value is pass with url like of resolutions data that also filter by resolutions type of data.

    url will pass like this for the param value 
    example: Main_category_api/?param_value=1
    '''
    param_value = request.GET.get("param_value", 0)
    if param_value:
        try:
            resolution_data = Resolutions.objects.get(id=param_value)
            allCategories = Categories.objects.filter(parent_category=None,Resolution=resolution_data)
        except:
            # allCategories = Categories.objects.filter(parent_category=None)
            return Response({"status_code":0,"status_Msg":"Please Select valid Category"},status=status.HTTP_400_BAD_REQUEST)
    else:
        allCategories = Categories.objects.filter(parent_category=None)

    List_of_main_category = CategorySerializer(allCategories,many=True)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_main_category.data} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_sub_categories(request,getId):
    '''
    Get Sub Categories Based on main Categories Id pass with url
    '''
    allSubCategory = Categories.objects.filter(parent_category=getId)
    List_of_sub_category = CategorySerializer(allSubCategory,many=True)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_sub_category.data} ,status=status.HTTP_200_OK)


@api_view(['GET'])
def list_of_images_based_on_category(request,subCategory):
    '''
    Get the List of Images and files based on the category
    '''
    recommended_image = DataStorage.objects.filter(parent_category=subCategory)
    List_of_image = List_for_data_store(recommended_image)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)