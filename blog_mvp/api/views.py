from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
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
def PostApi(req, id=0):
    if req.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)

        return JsonResponse(posts_serializer.data, safe=False)

    elif req.method == 'POST':
        post_data = JSONParser().parse(req)

        post_serializer = PostSerializer(data=post_data, partial=True)
        print(post_serializer.is_valid())
        if post_serializer.is_valid():
            print('valido')
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
            post = Post.objects.get(id=id)
            post.delete()
            return JsonResponse({'message': 'Deleted successfully!!'}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def SaveImage(request, id):
    file = request.FILES.get('image')  
    file_extension = os.path.splitext(file.name)[1]

    file_extension = os.path.splitext(file.name)[1]
    new_file_name = f"post_{id}{file_extension}"
    default_storage.save(new_file_name, file)

    destination_path = os.path.join(settings.MEDIA_ROOT, new_file_name)
    post = Post.objects.get(id=id)
    post.image_path = destination_path
    post.contains_image = True
    post.save()

    return JsonResponse('Image added successfully!!', safe=False)
