from  rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the OrderItem model.
    """
    product = ProductSerializer(read_only=True)
    item_subtotal = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'item_subtotal']
        read_only_fields = ['item_subtotal']
        
    def get_item_subtotal(self, obj):
        return obj.item_subtotal
    
class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.
    """
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')
    
    def total(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    
    class Meta:
        model = Order
        fields = ['order_id','user', 'status', 'items', 'products', "total_price", 'created_date']
        # read_only_fields = ['total_amount']
        
    # def get_total_amount(self, obj):
    #     return obj.total_amount
    
    