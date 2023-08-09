from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def first_API(request):
    return Response({"Status":1,"msg":"Success"})
# from .models import Category, Subcategory, Brand, Product
# from .serializers import CategorySerializer, SubcategorySerializer, BrandSerializer, ProductSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class SubcategoryViewSet(viewsets.ModelViewSet):
#     queryset = Subcategory.objects.all()
#     serializer_class = SubcategorySerializer

# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
>>>>>>> 42730824292b9cc53d66012571fc521759564095
