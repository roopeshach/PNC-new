from django.shortcuts import render
from .models import governing_body_desc , executive_committee_desc , management_committee_desc, campus_authority_desc, Campus_Authorities_members, Management_committee_members, Executive_committee_members


# Create your views here.

def governing(request):
    governing_details = governing_body_desc.objects.all().first()
    exec_details = executive_committee_desc.objects.all().first()
    management_details = management_committee_desc.objects.all().first()
    ca_details = campus_authority_desc.objects.all().first()

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
    }

    return render(request, 'governing_body/governing-body.html' , context )