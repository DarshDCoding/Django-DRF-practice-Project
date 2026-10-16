import datetime

from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsView(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)
