from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from decouple import config
urlpatterns = [
    path("", include('app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(config('admin'), admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
