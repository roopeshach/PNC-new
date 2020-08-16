from django.shortcuts import render
from .models import governing_body_desc , executive_committee_desc , management_committee_desc, campus_authority_desc, Campus_Authorities_members, Management_committee_members, Executive_committee_members, First_Management_committee
from category.models import Department, Program, Custom_Page,Faculty, Institute
from home.models import SocialMedia,Content

# Create your views here.
departments = Department.objects.all().filter(is_active="T")
programs = Program.objects.all().filter(is_active="T")
pages = Custom_Page.objects.all().filter(is_active="T")
faculties = Faculty.objects.all()
institutes = Institute.objects.all()
sm = SocialMedia.objects.all().first()
content = Content.objects.all().first()


def governing(request):
    governing_details = governing_body_desc.objects.all().first()
    exec_details = executive_committee_desc.objects.all().first()
    management_details = management_committee_desc.objects.all().first()
    ca_details = campus_authority_desc.objects.all().first()
    first_committee = First_Management_committee.objects.all()
    exec_members = Executive_committee_members.objects.all()
    mc_members = Management_committee_members.objects.all()
    ca_members = Campus_Authorities_members.objects.all()
    context = {
        'governing_details' :governing_details,
        'exec_details':exec_details,
        'management_details':management_details,
        'ca_details':ca_details,
        'exec_members' : exec_members,
        'mc_members' : mc_members,
        'ca_members' : ca_members,
        'first_committee':first_committee,
        'departments': departments,
        'programs': programs,
        'pages': pages,
        'faculties': faculties,
        'institutes': institutes,
        'sm': sm,
        'content': content,
    }

    return render(request, 'governing_body/governing-body.html' , context)