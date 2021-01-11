from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('pnc-administration/', admin.site.urls),
    path('', include('home.urls'), name="home"),
    path('tinymce', include('tinymce.urls')),
    path('', include('category.urls')),
    path('', include('news.urls')),
    path('', include('dev.urls')),
    path('', include('contact.urls')),
    path('', include('publication.urls')),
    path('', include('library.urls')),
    path('', include('blog.urls')),
    path('', include('governing_body.urls')),
    path('', include('administration.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Prithivi Narayan Campus Admin Dashboard"
admin.site.index_title = "Administrator Page PNC"
