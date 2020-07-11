from django.shortcuts import render
from .models import Content, Slider, Description, Message_From_Chief , FAQ , aboutUs
from category.models import Department, Program, Custom_Page, Faculty, Institute
from news.models import Notice, News, Event
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
content = Content.objects.all().first()
desc = Description.objects.all().first()
slides = Slider.objects.all()
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
news = News.objects.all()[:20]
notices = Notice.objects.all()[:20]
events = Event.objects.all()[:20]
messages = Message_From_Chief.objects.all()
pages = Custom_Page.objects.all()
faculties = Faculty.objects.all()
institutes = Institute.objects.all()

context = {
    'content': content,
    'departments': departments,
    'slides': slides,
    'desc': desc,
    'programs': programs,
    'news': news,
    'notices': notices,
    'events': events,
    'messages': messages,
    'pages': pages,
    'faculties': faculties,
    'institutes': institutes

}


def index(request):
    return render(request, 'home/index.html', context)


def courses(request):
    search_query = request.GET.get("search_courses", "")
    s_department = Department.objects.all().filter(name__icontains=search_query)
    s_program = Program.objects.all().filter(name__icontains=search_query)
    courses = list(chain(s_department, s_program))
    page = request.GET.get('page', 1)
    paginator = Paginator(courses, 6)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    context_courses = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        # 's_department': s_department,
        # 's_program': s_program,
        'courses':courses
    }
    return render(request, 'home/courses.html', context_courses)


def faqs(request):
    faqs = FAQ.objects.all()
    context = {
        'content': content,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'faqs':faqs,

    }

    return render(request, 'home/faq.html', context)
    

def aboutus(request):
    about = aboutUs.objects.all().first()
    context = {
        'content': content,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'about':about


    }

    return render(request , 'home/aboutUs.html', context)