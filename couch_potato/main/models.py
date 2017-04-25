from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import post_init

from .tmdb import search_for_movie
from .apple import apple_search

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    description = models.TextField(default="undescribed")
    img_url = models.TextField(default="none")
    backdrop = models.TextField(default="none")
    
    apple_url = models.TextField(default="none")
    apple_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return "Name: " + self.name + " Number: " + str(self.number)
    
def intialize_movie(**kwargs):
    instance = kwargs.get('instance')
    options = search_for_movie(instance.name)
    apple_info = apple_search(instance.name)
    
    if len(options) > 0:
        instance.description = options[0]["overview"]
        instance.number = options[0]["id"]
        instance.name = options[0]["original_title"]
        instance.img_url = options[0]["poster_path"]
        instance.backdrop = options[0]["backdrop_path"]

        instance.apple_price = apple_info[0]        
        instance.apple_url = apple_info[1]        
    else:
        instance.number = 0
        instance.description = "Unable to locate description for this movie."

post_init.connect(intialize_movie, Movie)
