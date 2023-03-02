from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    m_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'm_discount']

    def get_m_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount()        
            