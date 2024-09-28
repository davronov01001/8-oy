from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    quantity = serializers.IntegerField(required=True)
    brand = serializers.CharField(max_length=100, required=True)
    quality = serializers.IntegerField(required=True)
    category_id = serializers.IntegerField(required=True)
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.quality = validated_data.get('quality', instance.quality)
        instance.category_id = validated_data.get('category_id', instance.category_id   )
        instance.save()
        return instance
    
