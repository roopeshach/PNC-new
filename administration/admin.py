from django.contrib import admin
from .models import Administration, Administrative_Staff, page_image


# Register your models here.


class page_image_tablularInline(admin.TabularInline):
    model = page_image

    class Meta:
        model = Administration


class Admin_admin(admin.ModelAdmin):
    inlines = [page_image_tablularInline]


admin.site.register(Administration,Admin_admin)
admin.site.register(Administrative_Staff)
