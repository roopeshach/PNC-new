from django.contrib import admin
from .models import Contact
# Register your models here.
class contact(admin.ModelAdmin):
    list_display = ['name' , 'date']
admin.site.register(Contact, contact)