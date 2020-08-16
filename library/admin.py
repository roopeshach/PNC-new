from django.contrib import admin
from .models import E_Resources , library_page , page_image , thesis_title 
# Register your models here.



admin.site.register(E_Resources)

class page_image_tablularInline(admin.TabularInline):
    model = page_image
    class Meta:
        model = library_page

class library_page_admin(admin.ModelAdmin):
    inlines = [page_image_tablularInline]
    
admin.site.register(library_page , library_page_admin)
admin.site.register(thesis_title)