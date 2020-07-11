from django.contrib import admin
from .models import  Staff
# Register your models here.
class staff(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['department' , 'program']

admin.site.register(Staff, staff)