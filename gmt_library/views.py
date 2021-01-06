from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'gmt_library/home.html')

def academician(request):
    acas = Academician.objects.all()
    return render(request,'gmt_library/academician.html', {'acas:', acas})

