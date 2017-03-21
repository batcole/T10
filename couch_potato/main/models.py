from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    
    def __str__(self):
        return "Name: " + self.name + " Number: " + str(self.number)
    
