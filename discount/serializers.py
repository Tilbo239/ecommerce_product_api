from rest_framework import serializers
from .models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()
    start_date = serializers.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],  # format accepté à l'entrée
        format="%d/%m/%Y %H:%M"            # format affiché à la sortie
    )
    end_date = serializers.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        format="%d/%m/%Y %H:%M"
    )
    
    class Meta:
        model = Discount
        fields = ['id', 'percentage', 'start_date', 'end_date', 'is_active']
        
    def get_is_active(self, obj):
        return obj.is_active()