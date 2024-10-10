from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.Serializer):
    class Meta:
        model = Video
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance