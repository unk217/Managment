from django.db import models
import datetime

# Create your models here.

class Inventory(models.Model):
    brand = models.CharField(max_length=10)
    number = models.PositiveIntegerField(blank=False)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    f_birth = models.DateField(default=datetime.date.today)
    creation_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=50)
    Disease_history = models.TextField(blank=True)
    
    def __str__(self):
        return self.brand
    
    