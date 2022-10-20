from dataclasses import field
from tkinter import Widget
from .models import VehicalType,brand,category_list,vehical_Variant,Vehical_Registration
from django import forms


class VehicalTypeForm(forms.ModelForm):
    class Meta:
        model  = VehicalType
        fields = '__all__'
        exclude = ('added_date',)

class brandform(forms.ModelForm):
    class Meta:
        model  = brand
        fields = '__all__'
        exclude = ('AddDate','UserId')

class category_listform(forms.ModelForm):
    class Meta:
        model  = category_list
        fields = '__all__'
        exclude = ('AddDate','UserId')

        
class vehical_Variantform(forms.ModelForm):
    class Meta:
        model  = vehical_Variant
        fields = '__all__'
        exclude = ('AddDate','UserId')

class Vehical_Registrationform(forms.ModelForm):
    class Meta:
        model  = Vehical_Registration
        fields = '__all__'
        exclude = ('AddDate','UserId', 'Owner_Driving_Licence', 'RCBOOK')


