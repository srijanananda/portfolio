from django.urls import path
from .views import admin_login, dashboard, admin_logout

urlpatterns = [
    path('login/', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', admin_logout, name='admin_logout'),
]
