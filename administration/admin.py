from django.contrib import admin
from .models import Administration, Administrative_Staff, page_image,alumni,alumni_images


# Register your models here.


class page_image_tablularInline(admin.TabularInline):
    model = page_image

    class Meta:
        model = Administration


class Admin_admin(admin.ModelAdmin):
    inlines = [page_image_tablularInline]


class AdminStaff(admin.ModelAdmin):
    list_display = ['name','Post','administrative_offices']
    list_filter = ['Post','administrative_offices']


class alumni_images_tablularInline(admin.TabularInline):
    model = alumni_images

    class Meta:
        model = alumni


class AdminAlumni(admin.ModelAdmin):
    inlines = [alumni_images_tablularInline]
    list_display = ['title']


admin.site.register(Administration,Admin_admin)
admin.site.register(Administrative_Staff,AdminStaff)
admin.site.register(alumni,AdminAlumni)
