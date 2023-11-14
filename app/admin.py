from django.contrib import admin
from .models import Blog, Analytics, Comment, Contact
# Register your models here.


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ('title', 'created', 'updated',)
    list_display_links = ('title',)
    list_per_page = 30


@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_per_page = 30


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created',)
    list_display_links = ('email',)
    search_fields = ('email',)
    list_per_page = 30


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created',)
    list_display_links = ('email',)
    search_fields = ('name', 'email',)
    list_per_page = 30
