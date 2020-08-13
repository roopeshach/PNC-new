from django.urls import path
from publication import views

urlpatterns = [
    path('publication/', views.viewPublication, name="Publication"),
    path('publication/<str:slug>', views.detailPublication, name="Publication Details"),
]