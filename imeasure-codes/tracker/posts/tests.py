from django.test import TestCase
from posts.models import Post, Schedules
from django.utils import timezone
from . import models


class PostsTest(TestCase):
    def create_post(self):
        return Post.objects.create(Date=timezone.now())


    def test_post_creation(self):
        a = self.create_post()
        self.assertTrue(isinstance(a,Post))
