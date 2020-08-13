from django.shortcuts import render
from .models import Department, Program, Custom_Page, Faculty, Institute, Syllabus, PageImage
from home.models import Content
from news.models import News, Notice, Event
from photos.models import DepartmentGallery, ProgramGallery
from staffs.models import Staff
from django.db.models import Q

# Create your views here.
content = Content.objects.all().first()
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")
faculties = Faculty.objects.all()
institutes = Institute.objects.all()


def aboutDepartment(request, slug):
    dept = Department.objects.get(slug=slug)
    news = News.objects.filter(
        Q(department=dept.id))[:4]
    notices = Notice.objects.filter(
        Q(department=dept.id))[:4]

    staffs = Staff.objects.all().filter(department__id=dept.id)

    images = DepartmentGallery.objects.all().filter(title__department=dept.id)[:18]

    syllabus = Syllabus.objects.all().filter(department=dept.id)
    context = {
        'content': content,
        'departments': departments,
        'dept': dept,
        'programs': programs,
        'pages': pages,
        'news': news,
        'notices': notices,
        'faculties': faculties,
        'institutes': institutes,
        'staffs': staffs,
        'images': images,
        'syllabus': syllabus,

    }
    return render(request, 'category/about.html', context)


def aboutProgram(request, slug):
    program = Program.objects.get(slug=slug)
    news = News.objects.filter(
        Q(program=program.id))[:4]
    notices = Notice.objects.filter(
        Q(program=program.id))[:4]
    staffs = Staff.objects.all().filter(program__id=program.id)
    images = ProgramGallery.objects.all().filter(title__program=program.id)[:18]
    syllabus = Syllabus.objects.all().filter(program=program.id)
    context_program = {
        'content': content,
        'departments': departments,
        'program': program,
        'programs': programs,
        'pages': pages,
        'news': news,
        'notices': notices,
        'staffs': staffs,
        'images': images,
        'syllabus': syllabus,
        'faculties': faculties,
        'institutes': institutes,
    }

    return render(request, 'category/aboutProgram.html', context_program)


def aboutCustom(request, slug):
    page = Custom_Page.objects.get(slug=slug)
    images = PageImage.objects.all().filter(custom_page=page.id)
    context_custom = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'page': page,
        'faculties': faculties,
        'institutes': institutes,
        'images': images,
    }

    return render(request, 'category/aboutCustom.html', context_custom)


def aboutFaculty(request, slug):
    fac = Faculty.objects.get(slug=slug)
    departments_of_faculty = Department.objects.all().filter(faculty=fac.id)
    context = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'fac': fac,
        'departments_of_faculty': departments_of_faculty,

    }

    return render(request, 'category/aboutFaculty.html', context)


def aboutInstitute(request, slug):
    ins = Institute.objects.get(slug=slug)
    departments_of_faculty = Department.objects.all().filter(institute=ins.id)
    context = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'ins': ins,
        'departments_of_faculty': departments_of_faculty,
    }

    return render(request, 'category/aboutIns.html', context)
