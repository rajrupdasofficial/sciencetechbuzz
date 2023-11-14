from django.contrib.sitemaps import Sitemap
from .models import Blog


class BlogPostSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()
