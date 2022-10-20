from dataclasses import field
from django import forms
from .models import User


class UserloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')


class adminloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)

