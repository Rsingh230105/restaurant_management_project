from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
    def validate_item_price(self, value):
        """ Ensure price is a positive number"""
        if value <0 :
            raise serializers.ValidationError("Price must be positive.")
        return value