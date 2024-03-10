from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255)