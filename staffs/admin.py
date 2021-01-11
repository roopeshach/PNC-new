from django.contrib import admin
from .models import Staff


# Register your models here.
class staff(admin.ModelAdmin):
    list_display = ['image_tag','name','email','phone']
    list_filter = ['department', 'program']
    readonly_fields = ['image_tag']


admin.site.register(Staff, staff)
