from rest_framework import serializers
from reviews.serializers import ReviewSerializer
from .models import Product, Category, ProductImage
from discount.serializers import DiscountSerializer
from discount.models import Discount



class CategorySerializer(serializers.ModelSerializer):
  """
    Serializer for the Category model.
  """
  class Meta :
    model = Category
    fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProductImage model.
    """

    # image_url: retrieve the URL of the image file.
    image_url = serializers.SerializerMethodField()

    class Meta:
      model = ProductImage
      fields = ['id', 'image_url', 'is_main']

    # get_image_url: retrieve the URL of the image file.
    def get_image_url(self, obj):
        """
        Retrieves the URL of the image associated with this ProductImage instance.
        """
        return obj.image_url()
    
class ProductSerializer(serializers.ModelSerializer):


  # A nested serializer to represent all images associated with the product.
  images = ProductImageSerializer(many=True, read_only=True)
  
  reviews = ReviewSerializer(many=True, read_only=True)
  final_price = serializers.SerializerMethodField()
  
  discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all(), required=False, allow_null=True)
  

  
  # discount_price = serializers.ReadOnlyField()

  class Meta :
    model = Product
    fields = ['id', 'category', 'name', 'description', 'price', 'stock_quantity', 'images','discount', 'final_price', 'reviews', 'created_date', 'updated_date']
    
  def get_final_price(self, obj):
        return obj.final_price


