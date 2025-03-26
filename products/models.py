from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings



class Category(models.Model):
  """
    The Category class represents a category for grouping related products.
  """
  name = models.CharField(max_length=100)
  description = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    """
    Returns a string representation of the category, typically its name.
    """
    return self.name

class Product(models.Model):
  """
    The Product class represents a product within a category.
  """

  name = models.CharField(max_length=100, blank=False, null=False)
  description = models.TextField(blank=True)
  price = models.FloatField()
  stock_quantity = models.PositiveIntegerField(validators=[MinValueValidator(0, message="Stock quantity cannot be negatif")])
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  
  def reduce_stock_quantity(self, quantity):
    """
      Reduces the stock quantity of the product when an order is placed.
      Raises a ValueError if the stock is insufficient.
    """
    if self.stock_quantity >= quantity:
      self.stock_quantity -= quantity
      self.save()
    else:
      raise ValueError("Stock insufficient")

  def __str__(self):
    """
        Returns a string representation of the product, typically its name.
    """
    return self.name


class ProductImage(models.Model):
    """
        The ProductImage class represents an image associated with a product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    is_main = models.BooleanField(default=False)

    def image_url(self):
        return self.image.url

