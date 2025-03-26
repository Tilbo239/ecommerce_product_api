
from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
  """
    Serializer for the Review model.
  """
  class Meta :
    model = Review
    fields = ['rating', 'comment', 'created_date', 'updated_date']
    read_only_fields = ['created_date', 'updated_date']

    

