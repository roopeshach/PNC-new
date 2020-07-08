from django.contrib import admin
from .models import Event, News, Notice , NewsImage , NoticeImage , EventImage


# Register your models here.
class EventImageTabularInline(admin.TabularInline):
    model = EventImage
    class Meta:
        model = Event
        
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageTabularInline]
    list_display = ['title', 'date']

class NewsImageTabularInline(admin.TabularInline):
    model = NewsImage
    class Meta:
        model = News
        
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageTabularInline]
    list_display = ['title', 'date']

class NoticeImageTabularInline(admin.TabularInline):
    model = NoticeImage
    class Meta:
        model = Notice
        
class NoticeAdmin(admin.ModelAdmin):
    inlines = [NoticeImageTabularInline]
    list_display = ['title', 'date']

admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Notice, NoticeAdmin)
