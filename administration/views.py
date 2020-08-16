from django.shortcuts import render
from home.models import SocialMedia,Content
from .models import Administration,Administrative_Staff,page_image
from category.models import Department, Program, Custom_Page,Faculty, Institute
# Create your views here.


def AdministrationView(request):
    details = Administration.objects.all()
    staffs = Administrative_Staff.objects.all()
    images = page_image.objects.all()
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    pages = Custom_Page.objects.all().filter(is_active="T")
    faculties = Faculty.objects.all()
    institutes = Institute.objects.all()
    sm = SocialMedia.objects.all().first()
    content = Content.objects.all().first()
    context = {
        'details': details,
        'staffs': staffs,
        'images': images,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'content': content,
    }
    return render(request,'administration/administration.html',context)
