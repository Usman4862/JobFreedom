from django.contrib import admin
from employees.models import Employeeprofile,EmployeeProject,Jobapplication
# Register your models here.
admin.site.register(Employeeprofile)
admin.site.register(EmployeeProject)
admin.site.register(Jobapplication)