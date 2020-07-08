from django.contrib import admin
from .models import DepartmentImage , DepartmentGallery , ProgramImage , ProgramGallery
# Register your models here.

class DepartmentGalleryTabularInline(admin.TabularInline):
    model = DepartmentGallery
    class Meta:
        model = DepartmentImage
        
class DepartmentImageAdmin(admin.ModelAdmin):
    inlines = [DepartmentGalleryTabularInline]
    list_display = ['image_title']

class ProgramGalleryTabularInline(admin.TabularInline):
    model = ProgramGallery
    class Meta:
        model = ProgramImage
        
class ProgramImageAdmin(admin.ModelAdmin):
    inlines = [ProgramGalleryTabularInline]
    list_display = ['image_title']



admin.site.register(DepartmentImage, DepartmentImageAdmin)
admin.site.register(ProgramImage, ProgramImageAdmin)