from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from .views import (
    PostApi,
)

app_name = "api"

router = routers.DefaultRouter()
router.register(r'post', PostApi, basename='post')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)