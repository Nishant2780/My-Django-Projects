from django import forms
from .models import User

class UserloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'Mobile_Number', 'Pincode')
       

class ownerloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'State')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'mb-3 form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'class':'mb-3 form-control',
            }),
            'State': forms.Select(attrs={
                
            }),

        }

class adminloginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)

