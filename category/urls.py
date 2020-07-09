from django.urls import path
from . import views

urlpatterns = [
    path('about/<str:slug>', views.aboutDepartment , name="aboutDepartment"),
    path('about_program/<str:slug>', views.aboutProgram , name="aboutProgram"),
    path('pages/<str:slug>', views.aboutCustom , name="aboutCustom"),
    path('faculty/<str:slug>', views.aboutFaculty , name="aboutFaculty"),
    path('institute/<str:slug>', views.aboutInstitute , name="aboutInstitute")
    
]
