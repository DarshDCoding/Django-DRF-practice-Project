from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

class BlogManager (admin.ModelAdmin):
    model = Blog
    list_display = ("title", "created_at", "updated_at")

class CommentManager(admin.ModelAdmin):
    model = Comment
    list_display = ("comment", "created_at")

admin.site.register(Blog, BlogManager)
admin.site.register(Comment, CommentManager)