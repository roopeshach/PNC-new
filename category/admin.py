from django.contrib import admin
from .models import Department, Program, Custom_Page, Faculty, Institute, Syllabus,PageImage
from staffs.models import Staff


# Register your models here.

class StaffTabularInline(admin.TabularInline):
    model = Staff

    class Meta:
        model = Department


class PageImageTabularInline(admin.TabularInline):
    model = PageImage

    class Meta:
        model = Custom_Page


class PageAdmin(admin.ModelAdmin):
    inlines = [PageImageTabularInline]
    list_display = ['name']
    list_filter = ['is_active']


class department(admin.ModelAdmin):
    list_display = ['name', 'dean', 'faculty', 'institute']
    list_filter = ['faculty', 'institute']


class program(admin.ModelAdmin):
    list_display = ['name', 'dean', 'department', 'institute']
    list_filter = ['department', 'institute']


class faculty(admin.ModelAdmin):
    list_display = ['name', 'dean', 'header']


class institute(admin.ModelAdmin):
    list_display = ['name', 'dean', 'header']


class syllabus(admin.ModelAdmin):
    list_display = ['subject_name']
    list_filter = ['department']


admin.site.register(Faculty, faculty)
admin.site.register(Institute, institute)
admin.site.register(Department, department)
admin.site.register(Program, program)
admin.site.register(Custom_Page,PageAdmin)
admin.site.register(Syllabus, syllabus)
