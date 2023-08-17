from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('get_all_images/<str:deviceId>/',views.get_all_images),
    path('get_all_recommended_Imaging_list/<str:deviceId>/',views.get_all_recommended_Imaging_list),
    path('get_all_resolutions/',views.Get_all_resolutions),
    path('main_category_api/',views.Main_category_api),
    path('get_sub_categories/<int:getId>/',views.get_sub_categories),
    path('list_of_images_based_on_category/<int:subCategory>/<str:deviceId>/',views.list_of_images_based_on_category),
    path('list_of_images_based_on_resolution/<int:resolution>/<str:deviceId>/',views.list_of_images_based_on_resolution),
    path('add_and_remove_image_in_favorite/',views.add_and_remove_image_in_favorite),
    path('list_of_images_favorite/<str:deviceId>/',views.list_of_images_favorite),
]
