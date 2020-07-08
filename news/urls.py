from django.urls import path
from news import views

urlpatterns = [

    path('news/<str:slug>', views.viewNews, name="news"),
    path('news/', views.allNews, name="allNews"),
    path('notice/<str:slug>', views.viewNotice, name="notice"),
    path('notice/', views.allNotice, name="allNotice"),
    path('event/<str:slug>', views.viewEvent, name="event"),
]
