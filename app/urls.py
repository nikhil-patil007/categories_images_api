from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'subcategories', SubcategoryViewSet)
# router.register(r'brands', BrandViewSet)
# router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', views.first_API),
]
