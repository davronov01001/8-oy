from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

import io
from rest_framework.parsers import JSONParser


from .models import News


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
















# class News:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# news = News("Bu yerda nima", "Bu yerda nimadir boldi")
#
#
# class NewsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     content = serializers.CharField()
#
# def convert_to_json():
#     serializer = NewsSerializer(news)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#
# def json_to_python():
#     json = b'{"title":"Bu yerda nima","content":"Bu yerda nimadir boldi"}'
#     stream = io.BytesIO(json)
#     print(stream.read())
#     print(type(stream.read()))
#     data = JSONParser().parse(stream)
#     serializer = NewsSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)