from django.urls import path
from .views import admin_login, view_projects, add_project, admin_logout, delete_project

urlpatterns = [
    path('login/', admin_login, name='admin_login'),
    path('projects/', view_projects, name='view_projects'),
    path('add/', add_project, name='add_project'),
    path('delete/<int:project_id>/', delete_project, name='delete_project'),
    path('logout/', admin_logout, name='admin_logout'),
]
