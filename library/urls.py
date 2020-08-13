from django.urls import path
from library import views

urlpatterns = [
    path('library/', views.Library, name="Library"),
]