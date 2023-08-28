from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=65)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255)
    status = models.BooleanField(default=False)
    content = models.TextField()
    image_path = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    image_in_post_content = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts_created', null=True)
    updated_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    comment_user = models.ForeignKey('PostComments', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('post', 'tag')

class PostComments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name