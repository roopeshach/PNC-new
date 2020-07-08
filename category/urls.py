from django.urls import path
from . import views

urlpatterns = [
    path('about/<str:slug>', views.aboutDepartment , name="aboutDepartment"),
    path('about_program/<str:slug>', views.aboutProgram , name="aboutProgram"),
    path('pages/<str:slug>', views.aboutCustom , name="aboutCustom")
    
]
