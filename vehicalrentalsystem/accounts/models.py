from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


Status = (
    ('ahmedabad', 'ahmedabad'),
    ('Rajkot','Rajkot'),
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('hyderabad','hyderabad'),
    ('Goa','Goa'),
    ('vadodara','vadodara'),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    Mobile_Number = models.CharField(max_length=10, validators=[
                                     RegexValidator(r'^\d{10}$')])
    Rest_Name = models.CharField(max_length=80, null=True, blank=True)
    Address = models.CharField(max_length=200)
    State = models.CharField(max_length=20, choices=Status)
    Pincode = models.CharField(max_length=6, validators=[
        RegexValidator(r'^\d{6}$')])
    is_user = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name