from dataclasses import field
from tkinter import Widget
from admin_panel.models import Vehical_Registration
from django import forms



class Vehical_Registration_owner_form(forms.ModelForm):
    class Meta:
        model  = Vehical_Registration
        fields = '__all__'
        exclude = ('AddDate','UserId', 'Status')

class owner_VehicleDetails_form(forms.ModelForm):
    class Meta:
        model  = Vehical_Registration
        fields = '__all__'
        exclude = ('AddDate','UserId',)