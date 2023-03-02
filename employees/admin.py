from django.contrib import admin
from employees.models import EmployeeProfile, EmployeeProject, JobApplication

# Register your models here.
admin.site.register(EmployeeProfile)
admin.site.register(EmployeeProject)
admin.site.register(JobApplication)