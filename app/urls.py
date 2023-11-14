from django.urls import path
from .views import index, blogdetail, galleryview, contactview, aboutview
from app.sitemaps import BlogPostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'blogposts': BlogPostSitemap,
}


urlpatterns = [
    path("", index, name="indexpage"),
    path("<slug:slug>.html", blogdetail, name="article-detail"),
    path("artgallery", galleryview, name="gallery"),
    path("contact", contactview, name="contact"),
    path("about", aboutview, name="about"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
