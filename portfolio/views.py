from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from adminpanel.models import Project  # Import the model from adminpanel

def public_projects(request):
    projects = Project.objects.all()
    return render(request, 'public_projects.html', {'projects': projects})



def home(request):
    return render(request, 'home.html')

def info(request):
    return render(request, 'info.html')

def projects(request):
    return render(request, 'projects.html')
