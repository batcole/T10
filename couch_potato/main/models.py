from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import post_init

from .tmdb import search_for_movie

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    description = models.TextField(default="undescribed")
    
    def __str__(self):
        return "Name: " + self.name + " Number: " + str(self.number)
    
def intialize_movie(**kwargs):
    instance = kwargs.get('instance')
    options = search_for_movie(instance.name)

    if len(options) > 0:
        instance.description = options[0]["overview"]
        instance.number = options[0]["id"]
        instance.name = options[0]["original_title"]
    else:
        instance.description = "Unable to locate description for this movie."

post_init.connect(intialize_movie, Movie)
