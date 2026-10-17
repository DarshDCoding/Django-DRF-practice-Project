from django.contrib import admin

from employees.models import Employee, Subject

# Register your models here.

admin.site.register(Employee)
admin.site.register(Subject)