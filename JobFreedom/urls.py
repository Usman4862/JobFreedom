"""JobFreedom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from recruiters.views import  home, contact,post_job
from employees.views import browse_jobs, candidates, blogs, single_blog,want_job




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('browse/jobs/', browse_jobs, name="browse-jobs"),
    path('candidates/', candidates, name="candidates"),
    path('blogs/', blogs, name="blogs"),
    path('single/blogs/', single_blog, name="single-blog"),
    path('jobpost/',post_job,name='post-job'),
    path('wantjob/',want_job,name='want-job'),
    path('contact/', contact, name="contact"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)