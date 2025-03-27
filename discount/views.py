from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Discount
from .serializers import DiscountSerializer


class DiscountViewSet(viewsets.ModelViewSet):
  
  """
    A viewset for viewing and editing discount instances.
  """

  queryset = Discount.objects.all()
  serializer_class = DiscountSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]