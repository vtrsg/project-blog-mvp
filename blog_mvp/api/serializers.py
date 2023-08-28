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
        fields = ['username', 'email']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'status', 'content', 'image_in_post_content', 'image_path', 'created_at', 'category', 'tags']


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['name', 'content', 'created_at', 'author_id', 'post_id']