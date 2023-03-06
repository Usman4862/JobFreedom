from django.shortcuts import render
from .models import Recruiter
# Create your views here.


def home(request):
    return render(request, "index.html")

def browse_jobs(request):
    return render(request, "browsejobs.html")

def candidates(request):
    return render(request, "candidates.html")

def blogs(request):
    return render(request, "blog.html")

def single_blog(request):
    return render(request, "blog-single.html")

def contact(request):
    return render(request, "contact.html")
