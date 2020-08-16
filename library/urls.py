from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.Library, name="Library"),
    path('e-resources/',views.Resources,name="E_Resources"),
]