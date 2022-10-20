from collections import UserDict
from email import charset
from pyexpat import model
from statistics import mode
from unicodedata import category
from urllib.request import Request
from django.db import models
from django.forms import CharField
from accounts.models import User

# Create your models here.

class VehicalType(models.Model):
    Type_Name = models.CharField(max_length=50)
    Type_Image = models.ImageField(upload_to='type_img')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Type_Name

    class Meta:
        db_table = 'VehicalType'

class brand(models.Model):
    BrandName = models.CharField(max_length=50)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    AddDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.BrandName

    class Meta:
        db_table = 'brand'

class category_list(models.Model):
    Category_Name = models.CharField(max_length=50)
    AddDate = models.DateTimeField(auto_now_add=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Vehical_TypeID = models.ForeignKey(VehicalType, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.Category_Name

    class Meta:
        db_table = 'category_list'


fuel_type = (
    ('Diesel', 'Diesel'),
    ('Petrol', 'Petrol'),
    ('Electric', 'Electric'),
)

class vehical_Variant(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Vahical_Type = models.ForeignKey(VehicalType, on_delete=models.CASCADE)
    Variant_Name = models.CharField(max_length=50)
    Brand_n = models.ForeignKey(brand, on_delete=models.CASCADE)
    Vahical_catagory = models.ForeignKey(category_list, on_delete=models.CASCADE)
    Fuel_Type = models.CharField(max_length=10, choices=fuel_type)
    Seat_Capacity = models.IntegerField()
    Variant_Photo = models.ImageField(upload_to='Variant_img')
    Air_Condition = models.BooleanField(default=False)
    Power_Steering = models.BooleanField(default=False)
    Air_Bags = models.BooleanField(default=False)
    Power_Windows = models.BooleanField(default=False)
    Music_System = models.BooleanField(default=False)
    GPS_Location = models.BooleanField(default=False)
    AddDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Variant_Name


Status = (
    ('Pending', 'Pending'),
    ('Accepted','Accepted'),
    ('In Use','In Use'),
)

class Vehical_Registration(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    Vahical_Type = models.ForeignKey(VehicalType, on_delete=models.CASCADE,default=1)
    AddDate = models.DateTimeField(auto_now_add=True)
    vehical_Variant = models.ForeignKey(vehical_Variant, on_delete=models.CASCADE)
    Vehical_Number = models.CharField(max_length=10)
    Model_Year = models.IntegerField()
    KM_reading = models.BigIntegerField()
    Vehical_Orignal_img = models.ImageField(upload_to='Vehical_Orignal_img')
    Status = models.CharField(max_length=50, choices=Status, default='Pending')
    Owner_Driving_Licence = models.FileField(upload_to='Owner_Driving_Licence')
    RCBOOK = models.FileField(upload_to='RCBOOK')
    
    Prize = models.BigIntegerField()
    
    def __str__(self):
        return self.vehical_Variant.Variant_Name
    
