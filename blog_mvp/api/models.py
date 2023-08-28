from django.db import models
# import utils django
from django.utils.text import slugify
from django.utils import timezone
# import user model django
from django.contrib.auth.models import User
# import utils
from utils.utils_models import upload_image_to

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None,
        null=True, blank=True, max_length=255,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=65)
    subtitle = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    content = models.TextField()
    image_in_post_content = models.BooleanField(default=True)
    image_path = models.ImageField(upload_to=upload_image_to, blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts_created', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default='')
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title

class PostComments(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name