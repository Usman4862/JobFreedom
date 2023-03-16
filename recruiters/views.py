from django.shortcuts import render
from .models import Recruiter, JobCategory, JobPost
# Create your views here.


def home(request):
    categories = JobCategory.objects.all().order_by("id")
    jobposts = JobPost.objects.all().order_by("-created_at")
    context = {
        "jobcategories" : categories,
        "header_categories": categories[:5],
        "jobposts" : jobposts,
    }
    return render(request, "index.html", context=context)

def post_job(request):
    return render(request,'new-job-post.html')

def contact(request):
    return render(request, "contact.html")
