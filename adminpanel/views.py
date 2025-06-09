from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials or not a superuser.'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def admin_logout(request):
    logout(request)
    return redirect('home')
