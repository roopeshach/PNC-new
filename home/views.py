from django.shortcuts import render
from .models import Content , Slider , Description , Message_From_Chief
from category.models import Department , Program , Custom_Page
from news.models import Notice , News , Event

# Create your views here.
content = Content.objects.all().first()
desc = Description.objects.all().first()
slides = Slider.objects.all()
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
news = News.objects.all()[:3]
notices = Notice.objects.all()[:3]
events = Event.objects.all()[:3]
messages = Message_From_Chief.objects.all().first()
pages = Custom_Page.objects.all()

context = {
    'content' : content,
    'departments' : departments,
    'slides' : slides,
    'desc' : desc,
    'programs':programs,
    'news' :news,
    'notices':notices,
    'events':events,
    'messages' : messages,
    'pages':pages,

}

def index(request):
    return render(request , 'home/index.html', context)

