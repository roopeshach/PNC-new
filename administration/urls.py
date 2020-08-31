from . import views
from django.urls import path

urlpatterns = [
    path('administration/', views.AdministrationView, name="AdministrationView"),
    path('pnc-alumni/',views.Alumni,name="pnc_alumni"),
]