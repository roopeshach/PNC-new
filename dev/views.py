from django.shortcuts import render
from category.models import Department, Program, Custom_Page, Faculty, Institute
from home.models import Content, SocialMedia

# Create your views here.
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all()
faculties = Faculty.objects.all()
institutes = Institute.objects.all()
content = Content.objects.all().first()
sm = SocialMedia.objects.all().first()


def devs(request):
    context = {
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'content': content,
        'sm':sm,
    }
    return render(request, 'dev/dev.html', context)
