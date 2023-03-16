from django.contrib import admin
from .models import Recruiter, JobPost,JobCategory, Country, Company
# Register your models here.

admin.site.register(Recruiter)
admin.site.register(JobCategory)
admin.site.register(Country)
admin.site.register(Company)

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display= ['job_title', 'category']
