from django.db import models
import uuid
import os
# Create your models here.


def file_upload_location(instance, filename):
    file_description = instance.details.name.lower().replace(" ", "-")
    file_name = filename.lower().replace(" ", "-")
    return os.path.join("New_files", file_description, file_name)


class FileDetail(models.Model):
    name = models.CharField(max_length=255, default=None)
    number_folder = models.CharField(max_length=255, default=None)
    created = models.DateTimeField(auto_now_add=True)
    upadate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"file name {self.name}"


class FileUpload(models.Model):
    details = models.ForeignKey(FileDetail, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_upload_location, null=True, blank=True)

    def __str__(self) -> str:
        return f"name of files uploaded are {self.file}"


def photo_upload_location(instance, image_name):
    url = instance.details.name
    image_name = f'{uuid.uuid5(uuid.NAMESPACE_URL,url).hex}.jpg'
    return os.path.join('gallery_images', image_name)


class PhotoDetails(models.Model):
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upadate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"photo names are {self.name}"

    class Meta:
        verbose_name = 'Photo Detail'
        verbose_name_plural = 'Photo Details'


class Photo(models.Model):
    details = models.ForeignKey(PhotoDetails, default=None, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=photo_upload_location, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upadate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"photo details are {self.details}"
