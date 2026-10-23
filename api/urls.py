from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename="employee")

urlpatterns = [
    path('students/', views.studentsView, name="studentsView"),
    path('student_details/<int:pk>/', views.student_details, name='studentDetails'),
    path('', include(router.urls))
    # path('employees/', views.EmployeeView.as_view(), name='employees'),
    # path('employee_details/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_details'
]