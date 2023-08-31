from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.storage import default_storage

import os

# Import models
from django.contrib.auth.models import User
from .models import (
    Tag,
    Category,
    Post,
    PostComments
)
# Import serializers
from .serializers import (
    UserSerializer,
    TagSerializer,
    CategorySerializer,
    PostSerializer,
    PostCommentsSerializer
    )

@csrf_exempt
def LoginApi(req):
    if req.method == 'POST':
        user_data = JSONParser().parse(req)

        user = authenticate(username=user_data['username'], password=user_data['password'])

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return JsonResponse(access_token, safe=False, status=200)
        else:
            return JsonResponse('Invalid credentials', safe=False, status=401)
    return JsonResponse('Invalid method', safe=False, status=400)

@csrf_exempt
def LogonApi(req):
    if req.method == 'POST':
        user_data = JSONParser().parse(req)

        try:
            user = User.objects.create_user(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
            )

            user = authenticate(username=user_data['username'], password=user_data['password'])

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return JsonResponse(access_token, safe=False)
        except:
            return JsonResponse('Failed add!!', safe=False, status=400)
    return JsonResponse('Invalid method', safe=False, status=400)   

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def UserApi(req, id=0):
    if req.method == 'GET':
        if id != 0:
            user = User.objects.filter(id=id)
        else:
            user = User.objects.all()

        users_serializer = UserSerializer(user, many=True)
        return JsonResponse(users_serializer.data, safe=False)       
    elif req.method == 'PUT':
        user_data = JSONParser().parse(req)
        
        try:
            user = User.objects.get(id=id)
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()
            
            return JsonResponse('Updated successfully!!', safe=False)
        except User.DoesNotExist:
            return JsonResponse('User not found', safe=False, status=404)
    elif req.method == 'DELETE':
        try:
            User.objects.filter(id=id).update(is_active=False)

            return JsonResponse('User deleted successfully!!', safe=False)
        except User.DoesNotExist:
            return JsonResponse('User not found', safe=False, status=404)   
    else:
        return JsonResponse('Invalid request', safe=False, status=400)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def TagApi(req, id=0):
    if req.method == 'GET':
        if id != 0:
            tag = Tag.objects.filter(id=id)
        else:
            tag = Tag.objects.all()
        tags_serializer = TagSerializer(tag, many=True)

        return JsonResponse(tags_serializer.data, safe=False)    
    elif req.method == 'POST':
        tag_data = JSONParser().parse(req)
        tag_serializer = TagSerializer(data=tag_data)

        if tag_serializer.is_valid():
            tag_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'PUT':
        tag_data = JSONParser().parse(req)
        tag = Tag.objects.get(id=id)
        
        tag_serializer = TagSerializer(tag, data=tag_data)
        if tag_serializer.is_valid():
            tag_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        return JsonResponse('Failed update!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            tag = Tag.objects.get(id=id)
            tag.delete()
            
            return JsonResponse('Deleted successfully!!', safe=False)
        except Tag.DoesNotExist:
            return JsonResponse('Tag not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def CategoryApi(req, id=0):
    if req.method == 'GET':
        if id != 0:
            category = Category.objects.filter(id=id)
        else:
            category = Category.objects.all()
        categories_serializer = CategorySerializer(category, many=True)

        return JsonResponse(categories_serializer.data, safe=False)    
    elif req.method == 'POST':
        category_data = JSONParser().parse(req)
        category_serializer = CategorySerializer(data=category_data)

        if category_serializer.is_valid():
            category_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'PUT':
        category_data = JSONParser().parse(req)
        category = Category.objects.get(id=id)
        
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        return JsonResponse('Failed update!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            category = Category.objects.get(id=id)
            category.delete()
            
            return JsonResponse('Deleted successfully!!', safe=False)
        except Category.DoesNotExist:
            return JsonResponse('Category not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)
    
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostCommentsApi(req, id=0):
    if req.method == 'GET':
        if id != 0:
            comment = PostComments.objects.filter(id=id)
        else:
            comment = PostComments.objects.all()
        comments_serializer = PostCommentsSerializer(comment, many=True)

        return JsonResponse(comments_serializer.data, safe=False)    
    elif req.method == 'POST':
        comment_data = JSONParser().parse(req)
        comment_serializer = PostCommentsSerializer(data=comment_data)

        if comment_serializer.is_valid():
            comment_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            comment = PostComments.objects.get(id=id)
            comment.delete()
            
            return JsonResponse('Deleted successfully!!', safe=False)
        except PostComments.DoesNotExist:
            return JsonResponse('Comment not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostApi(req, id=0):
    if req.method == 'GET':
        if id != 0:
            posts = Post.objects.filter(id=id)
        else:
            posts = Post.objects.all()
            
        posts_serializer = PostSerializer(posts, many=True)

        return JsonResponse(posts_serializer.data, safe=False)
    elif req.method == 'POST':
        post_data = JSONParser().parse(req)

        post_serializer = PostSerializer(data=post_data, partial=True)
        if post_serializer.is_valid():
            post_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        return JsonResponse('Failed add!!', safe=False)
    elif req.method == 'PUT':
        post_data = JSONParser().parse(req)
        post = Post.objects.get(id=id)

        post_serializer = PostSerializer(post, data=post_data, partial=True)
        if post_serializer.is_valid():
            post_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        return JsonResponse('Failed update!!', safe=False)
    elif req.method == 'DELETE':
        try:
            Post.objects.filter(id=id).update(status=False)
            return JsonResponse('Deleted successfully!!', safe=False, status=200)
        except Post.DoesNotExist:
            return JsonResponse('Post not found', safe=False, status=404)
    else:
        return JsonResponse('Invalid method', safe=False, status=400)

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def SaveImage(req, id):
    if req.method == 'POST':
        file = req.FILES.get('image')  
        file_extension = os.path.splitext(file.name)[1]
        new_file_name = f"post_{id}{file_extension}"

        default_storage.save(new_file_name, file)
        destination_path = os.path.join(settings.MEDIA_ROOT, new_file_name)

        post = Post.objects.get(id=id)
        post.image_path = destination_path
        post.contains_image = True
        post.save()

        return JsonResponse('Image added successfully!!', safe=False)
    elif req.method == 'DELETE':
        post = Post.objects.get(id=id)
        os.remove(post.image_path)
        post.image_path = ''
        post.contains_image = False
        post.save()

        return JsonResponse('Deleted successfully!!', safe=False, status=200)
    else:
        return JsonResponse('Invalid method', safe=False, status=400)