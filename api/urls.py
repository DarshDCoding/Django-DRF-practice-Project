from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView, name="studentsView"),
    path('student/<int:pk>/', views.getStudent, name='getStudent'),
]