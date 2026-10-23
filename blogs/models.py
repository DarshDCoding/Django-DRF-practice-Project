from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment