from blog import views
from django.urls import path

urlpatterns = [
    path('blog/', views.blog, name="Blogs"),
    path('blog/<str:slug>', views.blogDetails, name="Blog Details")

]