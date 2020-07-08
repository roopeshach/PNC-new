from django.contrib import admin
from .models import Department , Program , Custom_Page , Faculty , Institute
# Register your models here.
class department(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'faculty']
    list_filter = ['faculty']

class program(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'department' , 'institute']
    list_filter = ['department' , 'institute']

class faculty(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header']

class institute(admin.ModelAdmin):
    list_display  = ['name' , 'dean' , 'header']
admin.site.register(Faculty, faculty)
admin.site.register(Institute, institute)
admin.site.register(Department, department)
admin.site.register(Program , program)
admin.site.register(Custom_Page)
