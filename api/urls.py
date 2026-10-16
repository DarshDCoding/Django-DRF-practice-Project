from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView, name="studentsView"),
    path('student_details/<int:pk>/', views.student_details, name='studentDetails'),
]