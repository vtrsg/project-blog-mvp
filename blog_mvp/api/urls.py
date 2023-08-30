from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from .views import (
    UserApi,
    TagApi,
    CategoryApi,
    PostCommentsApi,
    PostApi,
    SaveImage
)

app_name = "api"

urlpatterns = [
    path('user/', UserApi, name='user-list'),
    path('user/<int:id>/', UserApi, name='user-detail'),
    path('tag/', TagApi, name='tag-list'),
    path('tag/<int:id>/', TagApi, name='tag-detail'),
    path('category/', CategoryApi, name='category-list'),
    path('category/<int:id>/', CategoryApi, name='category-detail'),
    path('comments/', PostCommentsApi, name='post-comments-list'),
    path('comments/<int:id>/', PostCommentsApi, name='post-comments-detail'),
    path('post/', PostApi, name='post'),
    path('post/<int:id>/', PostApi, name='post-detail'),

    path('post/<int:id>/image/', SaveImage, name='save-image-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)