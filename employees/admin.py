from django.contrib import admin

from employees.models import Employee, Subject

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('name', 'designation', 'salary', 'joined_at')

class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('name',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Subject, SubjectAdmin)