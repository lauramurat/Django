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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Product
        fields = "__all__"

    # name = serializers.CharField(max_length=255)
    # slug = serializers.SlugField()
    # brand = serializers.CharField()
    # content = serializers.CharField()
    # photo = serializers.ImageField()
    # price = serializers.CharField(max_length=255)
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("title", instance.name)
    #     instance.slug = validated_data.get("slug", instance.slug)
    #     instance.brand = validated_data.get("brand", instance.brand)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.photo = validated_data.get("photo", instance.photo)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.cat = validated_data.get("cat", instance.cat)
    #     instance.save()
    #     return instance

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