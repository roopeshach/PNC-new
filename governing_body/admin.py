from django.contrib import admin
from .models import governing_body_desc, executive_committee_desc, management_committee_desc, campus_authority_desc, \
    Campus_Authorities_members, Management_committee_members, Executive_committee_members, First_Management_committee


class management_members(admin.ModelAdmin):
    list_display = ['name', 'member_role']


class executive_members(admin.ModelAdmin):
    list_display = ['name', 'member_role']


class authority_members(admin.ModelAdmin):
    list_display = ['name', 'member_role']


admin.site.register(First_Management_committee)
admin.site.register(governing_body_desc)
admin.site.register(executive_committee_desc)
admin.site.register(management_committee_desc)
admin.site.register(campus_authority_desc)
admin.site.register(Campus_Authorities_members, authority_members)
admin.site.register(Management_committee_members, management_members)
admin.site.register(Executive_committee_members, executive_members)
