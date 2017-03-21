from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Movie

# Create your views here.
from django.http import HttpResponse

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'main/detail.html', {'movie': movie})

def index(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'main/index.html', context)
