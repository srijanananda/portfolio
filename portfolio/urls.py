from django.urls import path
from .views import home,info,projects, public_projects

urlpatterns = [
    path('', home, name='home'),
    path('info/', info, name='info'),
    path('projects/', projects, name='projects'),
     path('public-projects/', public_projects, name='public_projects'),
]
