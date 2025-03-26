from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permi.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from rest_framework.validators import ValidationError
from .models import Review
from rest_framework.response import Response
from products.models import Product
from .serializers import  ReviewSerializer



class CreateReview(generics.CreateAPIView):
  """
Class CreateReview: A view for creating a new review for a product.

"""
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    pk = self.kwargs.get('pk')
    product = Product.objects.get(pk=pk)

    review_user = self.request.user
    review_queryset = Review.objects.filter(product=product, user=review_user)

    if review_queryset.exists():
      raise ValidationError("You can't review the same product twice.")

    serializer.save(product=product, user=review_user)
  
class ProductReviewList(generics.ListAPIView):
  """
Class:
    ProductReviewList: A view for listing all reviews for a specific product.
"""
    
  serializer_class = ReviewSerializer

  def get_queryset(self):
        
    pk = self.kwargs['pk']
    return Review.objects.filter(product=pk)


class ReviewList(generics.ListAPIView):
  """
    Class ReviewList: A view for listing all reviews.
  """
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  """
    Class ReviewDetail: A view for retrieving, updating, or deleting a specific review.
  """
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [IsOwnerOrReadOnly]




