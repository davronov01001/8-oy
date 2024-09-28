from rest_framework import serializers
from .models import Movie
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    quantity_of_actors = serializers.IntegerField(required=True)
    studio = serializers.CharField(max_length=100, required=True)
    rating = serializers.IntegerField(required=True)
    category_id = serializers.IntegerField(required=True)
    comment_id = serializers.IntegerField(required=True)
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.quantity_of_actors = validated_data.get('quantity_of_actors', instance.quantity_of_actors)
        instance.studio = validated_data.get('studio', instance.studio)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.category_id = validated_data.get('category_id', instance.category_id   )
        instance.comment_id = validated_data.get('comment_id', instance.comment_id   )
        instance.save()
        return instance
    
