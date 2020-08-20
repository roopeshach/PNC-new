from django.shortcuts import render
from django.http import HttpResponseRedirect
from category.models import Department, Program, Custom_Page, Faculty, Institute
from home.models import Content, SocialMedia
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse

departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all()
faculties = Faculty.objects.all()
institutes = Institute.objects.all()
content = Content.objects.all().first()
sm = SocialMedia.objects.all().first()


# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
        return HttpResponseRedirect('/contact-us/')
    context = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'content': content,
        'form': form,
        'sm':sm,
    }

    return render(request, 'contact/contact.html', context)
