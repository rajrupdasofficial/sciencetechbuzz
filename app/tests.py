from django.test import TestCase
from .models import TestModel

# Create your tests here.


class ModelTesting(TestCase):
    def setUp(self):
        self.blog = TestModel.objects.create(name="example title", bio="category", ex="content")

    def test_blog_model(self):
        data = self.blog
        self.assertTrue(isinstance(data, TestModel))
        self.assertEqual(str(data), 'example title')
