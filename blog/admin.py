from django.contrib import admin
from .models import Blog,International_Relation,PageImage,QAA


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'by']
    list_filter = ['date', 'by']


class PageImageTabularInline(admin.TabularInline):
    model = PageImage

    class Meta:
        model = International_Relation


class International(admin.ModelAdmin):
    inlines = [PageImageTabularInline]
    list_display = ['header']
    list_filter = ['is_active']


admin.site.register(International_Relation,International)
admin.site.register(Blog, BlogAdmin)
admin.site.register(QAA)
