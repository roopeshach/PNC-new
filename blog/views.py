from django.shortcuts import render
from home.models import SocialMedia,Content
from category.models import Department, Program, Custom_Page,Faculty, Institute
from .models import Blog,International_Relation,PageImage,QAA

# Create your views here.
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")
faculties = Faculty.objects.all()
institutes = Institute.objects.all()
sm = SocialMedia.objects.all().first()
content = Content.objects.all().first()


def blog(request):
    blog = Blog.objects.all()
    context_blog = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'blog': blog,
        'content':content,
    }
    return render(request,'blog/blog.html',context_blog)


def blogDetails(request, slug):
    blog = Blog.objects.get(slug=slug)
    context_blog = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'blog': blog,
        'content':content,
    }
    return render(request,'blog/blog-details.html',context_blog)


def International(request):
    international = International_Relation.objects.all()
    images = PageImage.objects.all()
    context_international = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'international': international,
        'images':images,
        'content':content,
    }
    return render(request,'blog/international-relation.html',context_international)


def QAAUnit(request):
    qaa = QAA.objects.all()
    context_qaa = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'qaa': qaa,
        'content':content,
    }
    return render(request,'blog/qaa.html',context_qaa)