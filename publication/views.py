from django.shortcuts import render
from home.models import SocialMedia,Content
from category.models import Department, Program, Custom_Page, Faculty, Institute
from .models import Publication,PublicationImage
from next_prev import next_in_order, prev_in_order
# Create your views here.


def viewPublication(request):
    publication = Publication.objects.all()
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    pages = Custom_Page.objects.all()
    faculties = Faculty.objects.all()
    institutes = Institute.objects.all()
    sm = SocialMedia.objects.all().first()
    content = Content.objects.all().first()
    context_publication = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm':sm,
        'publication':publication,
        'content':content,
    }
    return render(request, 'publication/publications.html',context_publication)


def detailPublication(request,slug):
    publication = Publication.objects.get(slug=slug)
    departments = Department.objects.all().filter(is_active="T")
    programs = Program.objects.all().filter(is_active="T")
    pages = Custom_Page.objects.all()
    faculties = Faculty.objects.all()
    institutes = Institute.objects.all()
    sm = SocialMedia.objects.all().first()
    previous = prev_in_order(publication)
    next = next_in_order(publication)
    images = PublicationImage.objects.all().filter(publication=publication.id)
    content = Content.objects.all().first()
    context_publication = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm':sm,
        'next': next,
        'previous': previous,
        'publication':publication,
        'images':images,
        'content':content,
    }
    return render(request, 'publication/publication-detail.html',context_publication)
