from dataclasses import field
from tkinter import Widget
from .models import ProductType,Products_Details, Comapany_Details, suppliers
from django import forms

class ProductsTypeForm(forms.ModelForm):
    class Meta:
        model  = ProductType
        fields = '__all__'
        exclude = ('added_date',)

class Products_Details_Form(forms.ModelForm):
    class Meta:
        model  = Products_Details
        fields = '__all__'
        exclude = ('added_date',)

class Comapany_Details_Form(forms.ModelForm):
    class Meta:
        model  = Comapany_Details
        fields = '__all__'

class suppliers_Form(forms.ModelForm):
    class Meta:
        model  = suppliers
        fields = '__all__' 
        exclude = ('User_id',)


        
        # widgets = {
        #     'StartDate': forms.DateInput(attrs={
        #         'type': 'date',
        #         'class': 'form-control'
        #     }),
        #     'EndDate': forms.DateInput(attrs={
        #         'type': 'date',
        #         'class': 'form-control'
        #     })
        # }


