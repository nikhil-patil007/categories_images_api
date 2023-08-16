from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *

# Create your views here.

def List_for_data_store(values):
    List_of_data = list()
    for arr in values:
        array_object = dict()
        array_object["id"] = arr.id
        array_object["type_of"] = arr.parent_category.type_of
        array_object["parent_category"] = arr.parent_category.name
        array_object["File"] = arr.file_url
        array_object["Recommended"] = arr.Recommended
        array_object["resolutions"] = arr.parent_category.Resolution.resolution
        List_of_data.append(array_object)

    return List_of_data

@api_view(["GET"])
def get_all_images(request):
    '''
     API For the Home Page to displayed the all images and Files.
    '''
    recommended_image = DataStorage.objects.all()
    List_of_image = List_for_data_store(recommended_image)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)

@api_view(["GET"])
def get_all_recommended_Imaging_list(request):
    '''
     API For the Home Page to displayed the recommended images and Files.
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
    List_of_resolutions = list()
    for i in getAllResolutions:
        res = dict()
        res['id'] = i.id
        res['resolution_name'] = i.resolution
        List_of_resolutions.append(res)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_resolutions} ,status=status.HTTP_200_OK)

@api_view(["GET"])
def Main_category_api(request):
    '''
    API for the getting List of main category.
    if resolution_id is pass with url like of resolutions data that also filter by resolutions type of data.

    url will pass like this for the param value 
    example: Main_category_api/?resolution_id=1
    '''
    resolution_id = request.GET.get("resolution_id", 0)
    if resolution_id:
        try:
            resolution_data = Resolutions.objects.get(id=resolution_id)
            allCategories = Categories.objects.filter(parent_category=None,Resolution=resolution_data)
        except:
            # allCategories = Categories.objects.filter(parent_category=None)
            return Response({"status_code":0,"status_Msg":"Please Select valid Category"},status=status.HTTP_400_BAD_REQUEST)
    else:
        allCategories = Categories.objects.filter(parent_category=None)

    List_of_main_category = list()
    # List_of_main_category = CategorySerializer(allCategories,many=True)
    for i in allCategories:
        res = {}
        res['id'] = i.id
        res['name'] = i.name
        res['type_of'] = i.type_of
        if(i.Resolution):
            res['resolution'] = i.Resolution.resolution
        else:
            res['resolution'] = ''
        res['parent_category'] = i.parent_category
        List_of_main_category.append(res)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_main_category} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_sub_categories(request,getId):
    '''
    Get Sub Categories Based on main Categories Id pass with url
    if resolution_id is pass with url like of resolutions data that also filter by resolutions type of data.

    url will pass like this for the param value 
    example: Main_category_api/?resolution_id=1
    '''
    resolution_id = request.GET.get("resolution_id", 0)
    if resolution_id:
        try:
            resolution_data = Resolutions.objects.get(id=resolution_id)
            allSubCategory = Categories.objects.filter(parent_category=getId,Resolution=resolution_data)
        except:
            # allCategories = Categories.objects.filter(parent_category=None)
            return Response({"status_code":0,"status_Msg":"Please Select valid Category"},status=status.HTTP_400_BAD_REQUEST)
    else:
        allSubCategory = Categories.objects.filter(parent_category=getId)

    List_of_sub_category = list()
    for i in allSubCategory:
        res = {}
        res['id'] = i.id
        res['name'] = i.name
        res['type_of'] = i.type_of
        if(i.Resolution):
            res['resolution'] = i.Resolution.resolution
        else:
            res['resolution'] = ''
        if(i.parent_category):
            res['parent_category'] = i.parent_category.name
        else:
            res['parent_category'] = ''
        List_of_sub_category.append(res)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_sub_category} ,status=status.HTTP_200_OK)


@api_view(['GET'])
def list_of_images_based_on_category(request,subCategory):
    '''
    Get the List of Images and files based on the category
    '''
    recommended_image = DataStorage.objects.filter(parent_category=subCategory)
    List_of_image = List_for_data_store(recommended_image)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_of_images_based_on_resolution(request,resolution):
    '''
    Get list of all image based on Resolutions.
    '''

    resolution_Image = DataStorage.objects.filter(Resolution=resolution)
    List_of_image = List_for_data_store(resolution_Image)
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)

@api_view(['POST'])
def add_and_remove_image_in_favorite(request):
    '''
    Create Api for the Add Image in the favorite database.
    if Device id and Image Id Is same Remove the Image from db.
    '''
    data = request.data
    image_id = data['image_id']
    device_id = data['device_id']

    Img_id = DataStorage.objects.filter(id=image_id)
    
    remove_img = Favorite.objects.filter(image_id =Img_id[0],device_id = device_id)
    if(remove_img):
        remove_img.delete()
        return Response({"status_code":1,"status_Msg": "Image Removed from Favorite"} ,status=status.HTTP_200_OK)

    add_img = Favorite.objects.create(        
        image_id =Img_id[0],
        device_id = device_id
    )
    return Response({"status_code":1,"status_Msg": "Image Add into Favorite"} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_of_images_favorite(request,deviceId):
    '''
    Get List of Favorite Images, Notifaction and Ringtones Using Device Id.
    '''
    getFavorite = Favorite.objects.filter(device_id = deviceId)
    List_of_image = list()
    for i in getFavorite:
        res = dict()
        res['id'] = i.id    
        res['file_id'] = i.image_id.id    
        res['file_type'] = i.image_id.parent_category.type_of 
        res['file_type'] = i.image_id.file_url
        res['file_category'] = i.image_id.parent_category.name
        res['file_resolution'] = i.image_id.Resolution.resolution
        List_of_image.append(res)   
    return Response({"status_code":1,"status_Msg": "Successful","data":List_of_image} ,status=status.HTTP_200_OK)

