from rest_framework import generics
from rest_framework.validators import ValidationError
from .models import Review
from rest_framework.response import Response
from products.models import Product
from .serializers import  ReviewSerializer


class CreateReview(generics.CreateAPIView):
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

  def perform_create(self, serializer):
    pk = self.kwargs.get('pk')
    product = Product.objects.get(pk=pk)

    review_user = self.request.user
    review_queryset = Review.objects.filter(product=product, user=review_user)

    if review_queryset.exists():
      raise ValidationError("You have already reviewed this product!")

    serializer.save(product=product, user=review_user)
  
class ProductReviewList(generics.ListAPIView):
    
  serializer_class = ReviewSerializer

  def get_queryset(self):
        
    pk = self.kwargs['pk']
    return Review.objects.filter(product=pk)


class ReviewList(generics.ListAPIView):
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

