from django.shortcuts import render
from .models import Department, Program, Custom_Page
from home.models import Content
from news.models import News, Notice, Event
from photos.models import DepartmentGallery 

from django.db.models import Q

# Create your views here.
content = Content.objects.all().first()
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")


def aboutDepartment(request, slug):
    dept = Department.objects.get(slug=slug)
    news = News.objects.filter(
        Q(department=dept.id))

    context = {
        'content': content,
        'departments': departments,
        'dept': dept,
        'programs': programs,
        'pages': pages,
        'news': news,

    }
    return render(request, 'category/about.html', context)


def aboutProgram(request, slug):
    program = Program.objects.get(slug=slug)
    news = News.objects.filter(
        Q(program=program.id))
    context_program = {
        'content': content,
        'departments': departments,
        'program': program,
        'programs': programs,
        'pages': pages,
        'news': news,
    }

    return render(request, 'category/aboutProgram.html', context_program)


def aboutCustom(request, slug):
    page = Custom_Page.objects.get(slug=slug)
    context_custom = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'page': page,
    }

    return render(request, 'category/aboutCustom.html', context_custom)
