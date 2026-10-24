from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename="employee")

blogrouter = DefaultRouter()
blogrouter.register('blogs', views.BlogViewSet, basename="blogs")

commentrouter = DefaultRouter()
commentrouter.register('comments', views.CommentViewset, basename='comment')

urlpatterns = [
    path('students/', views.studentsView, name="studentsView"),
    path('student_details/<int:pk>/', views.student_details, name='studentDetails'),
    path('', include(router.urls)),
    # path('employees/', views.EmployeeView.as_view(), name='employees'),
    # path('employee_details/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_details'
]

urlpatterns += blogrouter.urls
urlpatterns += commentrouter.urls