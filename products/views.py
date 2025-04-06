from rest_framework import viewsets,  filters
from django_filters.rest_framework import DjangoFilterBackend

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
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['category', 'stock_quantity', 'price']
  search_fields = ['name', 'category__name']
  ordering_fields = ['price', 'stock_quantity']
  permission_classes = [IsAuthenticatedOrReadOnly]

#   def get_object(self):
#         try:
#             return super().get_object()
#         except NotFound:
#             print("---------------Product not found-----------------")
#             raise NotFound({"error": "Sorry, this product is not available in our store."})



class ProductImageViewSet(viewsets.ModelViewSet):
  queryset = ProductImage.objects.all()
  serializer_class = ProductImageSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

