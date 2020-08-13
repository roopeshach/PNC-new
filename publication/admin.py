from django.contrib import admin
from .models import Publication,PublicationImage


# Register your models here.
class PublicationImageTabularInline(admin.TabularInline):
    model = PublicationImage

    class Meta:
        model = Publication


class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationImageTabularInline]
    list_display = ['title', 'date', 'department', 'program']
    list_filter = ['department', 'program']


admin.site.register(Publication, PublicationAdmin)
