from governing_body import views
from django.urls import path

urlpatterns = [
    path('governing-body/', views.Governing, name="Governing Body"),
]

