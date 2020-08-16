from blog import views
from django.urls import path

urlpatterns = [
    path('blog/', views.blog, name="Blogs"),
    path('blog/<str:slug>', views.blogDetails, name="Blog Details"),
    path('international-relation/', views.International,name="InternationalRelation"),
    path('QAA-Reform_Unit/',views.QAAUnit,name="QAA_Reform_Unit"),
]