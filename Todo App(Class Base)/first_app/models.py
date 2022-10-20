from django.db import models
from django.contrib.auth.models import User
# Create your models here.

category = (
    ('Indoor','Indoor'),
    ('Outdoor','Outdoor')
)

status = (
    ('On Going','On Going'),
    ('Completed','Completed')
)

class Task(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    Name = models.CharField(max_length = 100)
    Description = models.TextField()
    Category = models.CharField(max_length=10, choices = category)
    Create_date = models.DateField(auto_now_add=True)
    Complete_date = models.DateField(auto_now=True)
    Status = models.CharField(max_length = 10, choices = status, default = 'On Going')

    def __str__(self):
        return self.Name

    


