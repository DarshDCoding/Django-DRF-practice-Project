from django.http import JsonResponse
from students.models import Student
from api.serializers import StudentSerializer

# Create your views here.
def studentsView(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)
