from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Apartment(models.Model):
    CATEGORY_CHOICES = [
        ('3-bed', '3-bedroom'),
        ('2-bed', '2-bedroom'),
        ('1-bed', '1-bedroom'),
        ('Single', 'Single Room'),
        ('Bedsitter', 'Bedsitter')
    ]
    title = models.CharField(max_length=20, blank=False, null=False)
    location = models.CharField(max_length=200, blank=False, null=False)
    pricing = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="2-bed")
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {self.location}"
    

