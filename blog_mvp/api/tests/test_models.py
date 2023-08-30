# import testCase django
from django.test import TestCase
# import utils django
from django.utils import timezone
from django.utils.text import slugify
# import core files django
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
# import conf files django
from django.conf import settings
# import models 
from django.contrib.auth.models import User
from api.models import (
    Tag,
    Category,
    Post,
    PostComments
)
import os


class ModelApiTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email="teste@teste.com",
            password='testpassword',
            date_joined=timezone.now().isoformat()
        )
        self.category = Category.objects.create(name='TestCategory')
        self.tag = Tag.objects.create(name='TestTag')
        self.post = Post.objects.create(
            title='Test Post',
            subtitle='Test Subtitle',
            content='Test Content',
            created_by=self.user,
            category=self.category,
        )
        self.comment = PostComments.objects.create(
            name='Test Comment',
            content='Test Comment Content',
            author_id=self.user,
            post_id=self.post,
        )
        
    # Testando user 
    def test_user_delete_cascade_comments(self):
        initial_count = User.objects.count()

        self.user.delete()

        comment_count = PostComments.objects.filter(author_id=self.user).count()
        final_count = User.objects.count()

        self.assertEqual(comment_count, 0)  
        self.assertEqual(final_count, initial_count - 1)

    # Testando categoria 
    def test_category_slug(self):
        self.assertEqual(self.category.slug, slugify(self.category.name))

    def test_category_delete(self):
        initial_count = Category.objects.count()

        self.category.delete()

        final_count = Category.objects.count()

        self.post.refresh_from_db()
        
        self.assertEqual(final_count, initial_count - 1)
        self.assertIsNone(self.post.category)

    # Testando tag
    def test_tag_slug(self):
        self.assertEqual(self.tag.slug, slugify(self.tag.name))

    # Testando post comments
    def test_post_comments(self):
        self.assertEqual(self.comment.name, 'Test Comment')
        self.assertEqual(self.comment.content, 'Test Comment Content')
        self.assertEqual(self.comment.author_id, self.user)
        self.assertEqual(self.comment.post_id, self.post)
        self.assertTrue(isinstance(self.comment.created_at, timezone.datetime))

    # Testando post
    def test_post_created_at(self):
        self.assertTrue(isinstance(self.post.created_at, timezone.datetime))

    def test_post_category(self):
        self.assertEqual(self.post.category, self.category)

    def test_post_delete_cascade_comments(self):
        initial_count = Post.objects.count()

        self.post.delete()

        comment_count = PostComments.objects.filter(post_id=self.post).count()
        final_count = Post.objects.count()

        self.assertEqual(comment_count, 0)
        self.assertEqual(final_count, initial_count - 1)