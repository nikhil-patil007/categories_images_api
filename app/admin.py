from django.contrib import admin
from .models import *

# Register your models here.
class Categoriesadmin(admin.ModelAdmin):
    # model = Categories
    list_per_page = 15 # No of records per page 
    list_display = ('id','type_of','name','Resolution','parent_category')
    list_display_links = ('id','type_of','name','Resolution','parent_category')
    ordering = ('-id'),
    list_filter = ('type_of'),
    search_fields = ('name','Resolution','parent_category')
    
class DataStorageadmin(admin.ModelAdmin):
    # model = Files Store
    list_per_page = 15 # No of records per page 
    list_display = ('id','parent_category','file_view','Recommended')
    list_display_links = ('id','parent_category','file_view','Recommended')
    ordering = ('-id'),
    search_fields = ('parent_category',)


admin.site.register(Categories,Categoriesadmin)
admin.site.register(DataStorage,DataStorageadmin)
admin.site.register(Resolutions)
admin.site.register(Favorite)
# ABCD!123