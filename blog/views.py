from django.shortcuts import render
from home.models import SocialMedia
from category.models import Department, Program, Custom_Page,Faculty, Institute
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

# Create your views here.


def blog(request):
    blog = Blog.objects.all()
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    pages = Custom_Page.objects.all().filter(is_active="T")
    faculties = Faculty.objects.all()
    institutes = Institute.objects.all()
    sm = SocialMedia.objects.all().first()
    context_blog = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'blog': blog,
    }
    return render(request,'blog/blog.html',context_blog)


def blogDetails(request, slug):
    blog = Blog.objects.get(slug=slug)
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    pages = Custom_Page.objects.all().filter(is_active="T")
    faculties = Faculty.objects.all()
    institutes = Institute.objects.all()
    sm = SocialMedia.objects.all().first()
    context_blog = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'blog': blog,
    }
    return render(request,'blog/blog-details.html',context_blog)