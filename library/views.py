from django.shortcuts import render
from .models import E_Resources
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
    return render(request, 'library/library.html')


def Resources(request):
    resources = E_Resources.objects.all()
    context_resources = {
        'resources':resources,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm':sm,
        'content':content,
    }
    return render(request, 'library/e-resources.html',context_resources)
