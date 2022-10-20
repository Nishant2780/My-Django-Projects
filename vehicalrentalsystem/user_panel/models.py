from django.db import models
from accounts.models import *
from admin_panel.models import *

# Create your models here.

Status = (
    ('Pending', 'Pending'),
    ('Available','Available'),
)

class VehicalRequest(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    VehicalId = models.ForeignKey(Vehical_Registration, on_delete=models.CASCADE)
    RequestDate = models.DateTimeField(auto_now_add=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Pickup = models.CharField(max_length=20)
    Drop = models.CharField(max_length=20)
    Total_Price = models.IntegerField()
    Addhar_img = models.ImageField(upload_to='User_Addhar_img')
    Status = models.CharField(max_length=50, choices=Status, default='Pending')

    def __str__(self):
        return self.UserId