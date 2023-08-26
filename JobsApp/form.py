from django import forms

from .models import *

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model=ApplyJob
        fields=["Name","Email","CV","CoverLetter"]

class PostJobForm(forms.ModelForm):
    class Meta:
        model=Job
        
        fields='__all__'
        exclude=['slug','Owner']
          
        