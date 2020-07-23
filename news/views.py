from django.shortcuts import render
from news.models import News, Notice, Event, NewsImage , NoticeImage , EventImage
from photos.models import DepartmentGallery 
from category.models import Department, Program, Custom_Page,Faculty, Institute
from home.models import Content
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from next_prev import next_in_order, prev_in_order
# Create your views here.


content = Content.objects.all().first()
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")
faculties = Faculty.objects.all()
institutes = Institute.objects.all()
recent_news = News.objects.all()[:4]
recent_notice = Notice.objects.all()[:4]
gallery = DepartmentGallery.objects.all()[:12]


def viewEvent(request, slug):
    event = Event.objects.get(slug=slug)
    images = EventImage.objects.all().filter(event=event.id)

    context_event = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'event': event,
        'images': images,
        'faculties': faculties,
        'institutes': institutes,
        'recent_news':recent_news,
        'recent_notice':recent_notice,
        'gallery':gallery,
        
    }
    return render(request, 'news/events.html', context_event)


def allEvent(request):
    search_query = request.GET.get("search_event", "")

    event_list = Event.objects.all().filter(title__icontains=search_query)
    images = EventImage.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(event_list, 6)
    try:
        event = paginator.page(page)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)

    context_event = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'event': event,
        'images' :images,
        'faculties': faculties,
        'institutes': institutes
    }
    return render(request, 'news/allevents.html', context_event)


def viewNews(request, slug):

    news = News.objects.get(slug=slug)
    images = NewsImage.objects.all().filter(news=news.id)
   
    previous = prev_in_order(news)
    next = next_in_order(news)
    context_news = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'news': news,
        'images':images,
        'faculties': faculties,
        'institutes': institutes,
        'previous':previous,
        'next':next,
        'recent_news':recent_news,
        'recent_notice':recent_notice,
        'gallery':gallery,
    }
    return render(request, 'news/news.html', context_news)


def viewNotice(request, slug):
    notice = Notice.objects.get(slug=slug)
    images = NoticeImage.objects.all().filter(notice=notice.id)

    context_notice = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'notice': notice,
        'images' :images,
        'faculties': faculties,
        'institutes': institutes,
        'recent_news':recent_news,
        'recent_notice':recent_notice,
        'gallery':gallery,
       
    }
    return render(request, 'news/notice.html', context_notice)


def allNews(request):
    search_query = request.GET.get("search_news", "")
    news_list = News.objects.all().filter(title__icontains=search_query)

    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 6)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'news': news,
        'faculties': faculties,
        'institutes': institutes
    }
    print(news)
    return render(request, 'news/allnews.html', context)


def allNotice(request):
    search_query = request.GET.get("search_notice", "")
    notice_list = Notice.objects.all().filter(title__icontains=search_query)

    page = request.GET.get('page', 1)
    paginator = Paginator(notice_list, 6)
    try:
        notice = paginator.page(page)
    except PageNotAnInteger:
        notice = paginator.page(1)
    except EmptyPage:
        notice = paginator.page(paginator.num_pages)

    context = {
        'content': content,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'notice': notice,
        'faculties': faculties,
        'institutes': institutes
        
    }
    print(notice)
    return render(request, 'news/allnotice.html', context)
