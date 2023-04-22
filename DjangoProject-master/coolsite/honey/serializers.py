import io

from rest_framework import serializers
from .models import Product
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# class HoneyModel:
#     def __init__(self, name, content):
#         self.name = name
#         self.content = content


class HoneySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    brand = serializers.CharField()
    content = serializers.CharField()
    photo = serializers.ImageField()
    price = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat = serializers.IntegerField()


# def encode():
#     model = HoneyModel('Penka', 'Penka is a good')
#     model_sr = HoneySerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title: "Penka", "content": "Content: Penka is a good"}')
#     data = JSONParser().parse(stream)
#     serializers = HoneySerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)