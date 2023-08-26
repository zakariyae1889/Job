from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profiles
class SingUpForm(UserCreationForm):
    photo=forms.ImageField()
    phone=forms.CharField()
    city=forms.CharField()
    country=forms.CharField()
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'country',
            'city',
            'photo',
            'phone',
            'password1',
            'password2',
        ]
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            
        ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profiles
        fields=[
            'City',
            'Phone',
            'Photo',
        ]