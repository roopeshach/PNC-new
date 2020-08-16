from . import views
from django.urls import path

urlpatterns = [
    path('administration/', views.AdministrationView, name="AdministrationView"),
]