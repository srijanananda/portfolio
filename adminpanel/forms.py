from django import forms
from .models import Project

from .models import Info

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'link']



class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'