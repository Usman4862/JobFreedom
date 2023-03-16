from django.shortcuts import render
from .models import Recruiter
# Create your views here.


def home(request):
    return render(request, "index.html")

def post_job(request):
    return render(request,'new-job-post.html')

def contact(request):
    return render(request, "contact.html")
