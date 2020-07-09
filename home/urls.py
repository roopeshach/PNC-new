from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('courses/', views.courses, name="courses")
]


