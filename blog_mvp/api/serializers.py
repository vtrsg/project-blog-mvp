from rest_framework import serializers
# import models
from django.contrib.auth.models import User
from .models import (
    Tag,
    Category,
    Post,
    PostComments
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ['id', 'username', 'first_name', 'last_name',
                           'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    category = serializers.CharField()

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        category_name = validated_data.pop('category')

        post = Post.objects.create(**validated_data)

        # se os campos name tag não existir na tabela TAG ele cria e adiciona ao post, se não, só pega e adiciona.
        for tag in tags_data:
            tag_name = tag.get('name')
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        # se o campo name category não existir na tabela CATEGORY ele cria e adiciona ao post, se não, só pega e adiciona.
        category, created = Category.objects.get_or_create(name=category_name)
        post.category = category
        post.save()

        return post


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'