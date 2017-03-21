from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Movie
from .tmdb import *

# Create your views here.
from django.http import HttpResponse

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'main/detail.html', {'movie': movie})

def index(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'main/index.html', context)

def show_movie(request, movie_number):
    # TODO implement this method to properly get data. wire it up to some
    # urls on a page, with templates.
    data = tmdb.get_movie(movie_number)
    context = {}
    return render(request, 'main/movie_template.html', context)
