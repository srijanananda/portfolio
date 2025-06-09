from django.urls import path
from .views import home,info,projects

urlpatterns = [
    path('', home, name='home'),
    path('info/', info, name='info'),
    path('projects/', projects, name='projects'),
]
