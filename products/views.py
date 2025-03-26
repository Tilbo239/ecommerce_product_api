from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from permi.permissions import IsAdminOrReadOnly
from .models import Product, Category, ProductImage
from .serializers import  ProductImageSerializer, ProductSerializer, CategorySerializer



  

class CategoryViewSet(viewsets.ModelViewSet):
  
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
  
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]


class ProductImageViewSet(viewsets.ModelViewSet):
  queryset = ProductImage.objects.all()
  serializer_class = ProductImageSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

