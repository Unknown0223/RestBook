from rest_framework import serializers
from .models import Author, Category, Book

class AuthorSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True) 
    first_name = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    age = serializers.IntegerField(allow_null=False)
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, validated_data, instance):
        instance.first_name = validated_data.get('first_name', instance.first_name) 
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    category_id = serializers.IntegerField(allow_null=True)
    author_id = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
