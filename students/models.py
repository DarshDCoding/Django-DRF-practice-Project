from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=20)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.student_id