from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.shortcuts import get_object_or_404
from django.urls import reverse

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_superuser:
            login(request, user)
            return redirect('view_projects')
        else:
            return render(request, 'adminpanel/login.html', {'error': 'Invalid credentials or not a superuser'})
    return render(request, 'adminpanel/login.html')

@login_required
def view_projects(request):
    projects = Project.objects.all()
    return render(request, 'adminpanel/view_projects.html', {'projects': projects})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_projects')
    else:
        form = ProjectForm()
    return render(request, 'adminpanel/add_project.html', {'form': form})


def admin_logout(request):
    logout(request)
    return redirect(reverse('home')) 

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('view_projects')