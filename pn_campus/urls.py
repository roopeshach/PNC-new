"""pn_campus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Pnc-Administration/', admin.site.urls),
    path('', include('home.urls'), name="home"),
    path('tinymce', include('tinymce.urls')),
    path('', include('category.urls')),
    path('', include('news.urls')),
    path('', include('dev.urls')),
    path('', include('contact.urls')),
    path('', include('publication.urls')),
    path('',include('library.urls')),
    path('',include('blog.urls')),
    path('',include('governing_body.urls')),
    path('',include('administration.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "PNC Admin"
admin.site.site_title = "PNC Admin"
admin.site.index_title = "Administrator Page PNC"