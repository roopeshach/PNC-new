from django.contrib import admin
from .models import Department , Program , Custom_Page
# Register your models here.
class department(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header' , 'id']

class program(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header']



admin.site.register(Department, department)
admin.site.register(Program , program)
admin.site.register(Custom_Page)
