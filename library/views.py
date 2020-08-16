from django.shortcuts import render
from .models import E_Resources,library_page,page_image,thesis_title
from category.models import Department, Program, Custom_Page,Faculty, Institute
from home.models import SocialMedia,Content


# Create your views here.
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")
faculties = Faculty.objects.all()
institutes = Institute.objects.all()
sm = SocialMedia.objects.all().first()
content = Content.objects.all().first()


def Library(request):
    library = library_page.objects.all()
    thesis = thesis_title.objects.all()

    images = page_image.objects.all()
    context_library = {
        'library': library,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm':sm,
        'content':content,
        'images':images,
        'thesis':thesis,
    }
    return render(request, 'library/library.html',context_library)


def Resources(request):
    resources = E_Resources.objects.all()
    images = page_image.objects.all()
    context_resources = {
        'resources':resources,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm':sm,
        'content':content,
        'images':images,
    }
    return render(request, 'library/e-resources.html',context_resources)
