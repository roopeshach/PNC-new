from . import views
from django.urls import path

urlpatterns = [
    path('contact-us/', views.contact, name="contact")
]


