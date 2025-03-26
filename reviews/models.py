from django.db import models
from products.models import Product
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
  """
    The Review classnrepresents a user reviewed a product.
  """
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  comment = models.TextField(blank=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)