from django.contrib import admin
from .models import Content, Slider, Description, Message_From_Chief


# Register your models here.
class content(admin.ModelAdmin):
    list_display = ['email', 'phone', 'address']


class sliderContent(admin.ModelAdmin):
    list_display = ['head', 'photo']


class descView(admin.ModelAdmin):
    list_display = ['header']


class message(admin.ModelAdmin):
    list_display = ['chief_name']


admin.site.register(Content, content)
admin.site.register(Slider, sliderContent)
admin.site.register(Description, descView)
admin.site.register(Message_From_Chief, message)
