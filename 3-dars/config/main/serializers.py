from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io



# class News:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

# news = News("Bu yerda nima?", "Bu yerda nimadur bolgani anniq")
# print(news)

# class NewSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=3)
#     content = serializers.CharField()

# def convert_to_json():
#     serializer = NewSerializer(news)
#     print(serializer.data)

#     json = JSONRenderer().render(serializer.data)
#     print(json)
# def json_to_python():
#     json = b'{"title":"Bu yerda nima?","content":"Bu yerda nimadur bolgani anniq"}'
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     serializer = NewSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     print(serializers.validated_data())

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
