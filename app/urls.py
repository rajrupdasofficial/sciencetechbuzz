from django.urls import path
from .views import index, blogdetail, galleryview, contactview, aboutview, robots_txt
from .sitemaps import StaticViewSitemap, BlogSitemap, CategorySitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'category': CategorySitemap,
}


urlpatterns = [
    path("", index, name="indexpage"),
    path("<str:category>/<slug:slug>", blogdetail, name="article-detail"),
    path("artgallery", galleryview, name="gallery"),
    path("contact", contactview, name="contact"),
    path("about", aboutview, name="about"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt)
]
