from django.shortcuts import render

# Create your views here.
def devs(request):
    return render(request, 'dev/dev.html')