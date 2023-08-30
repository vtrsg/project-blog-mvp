from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from .views import (
    PostApi,
    SaveImage
)

app_name = "api"

urlpatterns = [
    path('post/', PostApi, name='post'),
    path('post/<int:id>/', PostApi, name='post-detail'),

    path('post/<int:id>/image/', SaveImage, name='save_image_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)