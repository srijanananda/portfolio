from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def projects(request):
    return render(request, 'projects.html')
