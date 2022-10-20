from admin_panel.models import ProductType,Products_Details, Comapany_Details, suppliers
from .models import *
from django import forms
from dataclasses import field


class quotations_Form(forms.ModelForm):
    class Meta:
        model  = quotations
        fields = '__all__'
        exclude = ('added_date','User_id','Status','Profit',)
