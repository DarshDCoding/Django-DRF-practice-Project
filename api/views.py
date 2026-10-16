import datetime

from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from students.serializers import StudentSerializer

# Create your views here.
def studentsView(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)
