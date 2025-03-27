
from rest_framework import serializers
from .models import Product, Review
from users.serializers import LoginUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
  """"
  Serializer for the Review model.
  """
#   user = LoginUserSerializer(read_only=True)

  class Meta :
    model = Review
    fields = [
      'rating', 
      'comment', 
      'created_date', 
      'updated_date', 
    #   'user'
    ]
    # fields = '__all__'
    # depth = 1
    read_only_fields = ['created_date', 'updated_date']

    

