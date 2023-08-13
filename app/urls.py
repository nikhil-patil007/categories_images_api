from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page_api),
    path('main_category_api/',views.Main_category_api),
    path('get_all_resolutions/',views.Get_all_resolutions),
    path('get_sub_categories/<int:getId>/',views.get_sub_categories),
    path('list_of_images_based_on_category/<int:subCategory>/',views.list_of_images_based_on_category),
]
