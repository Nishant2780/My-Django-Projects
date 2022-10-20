from collections import UserDict
from pyexpat import model
from statistics import mode
from urllib.request import Request
from django.db import models
from django.core.validators import RegexValidator
from accounts.models import *
from .models import *

# Create your models here


class ProductType(models.Model):
    products_types = models.CharField(max_length=50)
    product_types_img = models.ImageField(upload_to='type_img')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.products_types

class suppliers(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    suppliers_name = models.CharField(max_length=15)
    suppliers_contact = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$')])
    suppliers_goods = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)
    business_number = models.CharField(max_length=15)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.suppliers_name


class Products_Details(models.Model):
    ProductType = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    Products_Name = models.CharField(max_length=50)
    Products_Image = models.ImageField(upload_to='products_img')
    Products_quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now_add=True) 
    Products_base_price = models.BigIntegerField()
    Products_selling_price = models.BigIntegerField()
    suppliers_id = models.ForeignKey(suppliers, on_delete=models.CASCADE)

    def __str__(self):
        return self.Products_Name

    def tax_amount(self):


        gst_amt = ( self.Products_base_price * 18 ) / 100
        Price = self.Products_base_price + gst_amt

        return Price

class Comapany_Details(models.Model):
    Comapany_Name = models.CharField(max_length=15)
    Company_address = models.CharField(max_length=60)
    Company_phone_number = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$')])
    gst_numbe = models.CharField(max_length=15)

    def __str__(self):
        return self.Comapany_Name




    





    
