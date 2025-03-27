from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
# from django.utils import timezone
from discount.models import Discount


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
    stock_quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(0, message="Stock quantity cannot be negatif")]
    )
    
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
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
        
    @property
    def final_price(self):
        """Apply discount only if it's active within the time interval."""
        if self.discount and self.discount.is_active():
            return self.price - (self.price * (self.discount.percentage / 100))
        return self.price


    # @property
    # def discount_price(self):
    #     """
    #     Calculates and returns the discounted price if there is an active discount.
    #     """
    #     now = timezone.localtime(timezone.now())

    #     # Get the first active discount for the product.
    #     discount = self.discounts.filter(
    #         start_date__lte=now, end_date__gte=now
    #     ).first()

    #     # If there is an active discount, apply it to the price.
    #     if discount:
    #         return discount.apply_discount(self.price)
    #     return self.price

    def __str__(self):
        """
        Returns a string representation of the product, typically its name.
        """
        return f"{self.name} - Final Price: {self.final_price}"


class ProductImage(models.Model):
    """
    The ProductImage class represents an image associated with a product.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="products/")
    is_main = models.BooleanField(default=False)

    def image_url(self):
        return self.image.url
