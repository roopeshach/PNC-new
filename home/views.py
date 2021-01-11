from django.shortcuts import render
from .models import Content, Slider, Description, Message_From_Chief , FAQ , aboutUs, SocialMedia,Campus_Chiefs_to_date,PageImage,Preloader
from category.models import Department, Program, Custom_Page, Faculty, Institute
from news.models import Notice, News, Event
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from staffs.models import Staff
# Create your views here.
content = Content.objects.all().first()
desc = Description.objects.all().first()
slides = Slider.objects.all()
loader = Preloader.objects.filter(is_active="T")[:1]
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all()
faculties = Faculty.objects.all()
institutes = Institute.objects.all()

news = News.objects.all()[:20]
notices = Notice.objects.all()[:20]
events = Event.objects.all()[:20]
messages = Message_From_Chief.objects.all()


d_c = departments.count()
p_c = programs.count()
courses_c = d_c + p_c
staffs = Staff.objects.all().count()
about = aboutUs.objects.all().first()

sm = SocialMedia.objects.all().first()
context = {
    'content': content,
    'loader':loader,
    'departments': departments,
    'programs': programs,
    'pages': pages,
    'faculties': faculties,
    'institutes': institutes,
    'slides': slides,
    'desc': desc,
    'news': news,
    'notices': notices,
    'events': events,
    'messages': messages,
    'courses':courses_c,
    'staffs':staffs,
    'about':about,
    'sm':sm,
}


def index(request):
    print('loader:',loader)
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
        'faqs': faqs,
        'sm':sm,
    }
    return render(request, 'home/faq.html', context)
    

def aboutus(request):
    about = aboutUs.objects.all().first()
    images = PageImage.objects.all()
    context = {
        'content': content,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'about':about,
        'images':images,
    }
    return render(request , 'home/aboutUs.html', context)


def Message(request):
    chiefs = Campus_Chiefs_to_date.objects.all()
    context_message = {
        'content': content,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'messages': messages,
        'chiefs': chiefs,
        'sm':sm,
    }
    return render(request, 'home/message.html', context_message)
