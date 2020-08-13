from django.shortcuts import render


# Create your views here.
def Governing(request):
    return render(request,'governing_body/governing-body.html')