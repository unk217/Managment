from django.db import models
import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50 )
    
    def __str__(self):
        return self.first_name

class Inventory(models.Model):
    brand = models.CharField(max_length=10)
    number = models.PositiveIntegerField(blank=False)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    f_birth = models.DateField(default=datetime.date.today)
    creation_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    Disease_history = models.TextField(blank=True)
    
    def age_r(self):
        today = datetime.date.today()
        delta = relativedelta(today, self.f_birth)
        return f"{delta.years} años, {delta.months} meses y {delta.days} dias"
    
    def __str__(self):
        return self.brand
    

    
    
     
    
    