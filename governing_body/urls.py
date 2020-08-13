from governing_body import views
from django.urls import path

urlpatterns = [
    path('governing-body/', views.governing, name="GoverningBody"),
]

