from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class PostApi(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=True, methods=['put'])
    def custom_put(self, request, pk=None):
        return self.custom_put_method(request, pk=pk)

    @action(detail=True, methods=['delete'])
    def custom_delete(self, request, pk=None):
        return self.custom_delete_method(request, pk=pk)
