from django.contrib import admin
from .models import (FileUpload, FileDetail, Photo, PhotoDetails, )


class FileAdmin(admin.StackedInline):
    model = FileUpload


@admin.register(FileDetail)
class DetailAdmin(admin.ModelAdmin):
    inlines = [FileAdmin]


@admin.register(FileUpload)
class UploadAdmin(admin.ModelAdmin):
    list_per_page = 30


class PhotoAdmin(admin.StackedInline):
    model = Photo


@admin.register(PhotoDetails)
class PhotoDetailAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]


@admin.register(Photo)
class PhotoUploadAdmin(admin.ModelAdmin):
    list_per_page = 30
