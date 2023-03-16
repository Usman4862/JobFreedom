from django.shortcuts import render
from recruiters.models import JobPost
from employees.models import EmployeeProfile
# Create your views here.
def browse_jobs(request):
    jobs = JobPost.objects.all()
    context = {
        'Jobs': jobs,
        }
    
    return render(request, "browsejobs.html", context=context)

def candidates(request):
    employees = EmployeeProfile.objects.all()
    context = {
        'employees' : employees,
    }
    return render(request, "candidates.html", context=context)

def blogs(request):
    return render(request, "blog.html")

def single_blog(request):
    return render(request, "blog-single.html")

def want_job(request):
    jobs = JobPost.objects.all()
    context = {
        'Jobs': jobs,
    }
    return render(request, 'want-job.html', context=context)

