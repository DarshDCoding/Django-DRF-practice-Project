from django.contrib import admin

from employees.models import Employee, Subject

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'salary', 'joined_at')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Subject)