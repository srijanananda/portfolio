from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def info(request):
    return HttpResponse("<h2>This is info page</h2>")

def projects(request):
    return HttpResponse("<h2>This is projects page</h2>")
