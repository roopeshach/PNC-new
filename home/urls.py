from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('courses/', views.courses, name="courses"),
    path('frequently-asked-questions/',views.faqs,name="frequently asked questions"),
    path('about-us/', views.aboutus, name="aboutus"),
]


