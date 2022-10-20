from telnetlib import STATUS
from django.db import models
from requests import request
# from SaleManagementSystem.admin_panel.models import Products_Details
from accounts.models import *
from admin_panel.models import *

# Create your models here.
Status = (
    ('Pending', 'Pending'),
    ('Accepted','Accepted'),

)

class quotations(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Products_Details, on_delete=models.CASCADE)
    Product_price = models.BigIntegerField()
    Product_quantity = models.BigIntegerField()
    Profit = models.BigIntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50, choices=Status, default='Pending')
    Customer_Name = models.CharField(max_length=120)
    Custumer_contact = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{10}$')])
    


    

