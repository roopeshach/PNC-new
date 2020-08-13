from django.contrib import admin
from .models import committee,committee_member,committee_role

# Register your models here.

admin.site.register(committee)
admin.site.register(committee_member)
admin.site.register(committee_role)