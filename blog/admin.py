from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'by']
    list_filter = ['date', 'by']


admin.site.register(Blog, BlogAdmin)
