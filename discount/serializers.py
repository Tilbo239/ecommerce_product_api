from rest_framework import serializers
from .models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()
    
    class Meta:
        model = Discount
        fields = ['id', 'percentage', 'start_date', 'end_date', 'is_active']
        
    def get_is_active(self, obj):
        return obj.is_active()