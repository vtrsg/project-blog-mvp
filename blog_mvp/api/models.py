from django.db import models
# import utils django
from django.utils.text import slugify
from django.utils import timezone
# import user model django
from django.contrib.auth.models import User
# import utils
#from utils.utils_models import upload_image_to
import os

class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, default=None,
        null=True, blank=True, max_length=255,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=65, null=False, blank=False)
    subtitle = models.CharField(max_length=255, null=False, blank=False)
    status = models.BooleanField(default=False, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image_path = models.CharField(max_length=100)
    contains_image = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts_created', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default='')
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title
    

class PostComments(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name