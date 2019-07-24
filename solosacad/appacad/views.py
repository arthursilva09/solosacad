from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def abc(request):
    return HttpResponse('Hello!')

def prof(request, nome):
    return render(request, 'appacad/prof.html', {'nome':nome})

def home(request):
    return render(request, 'appacad/index.html')