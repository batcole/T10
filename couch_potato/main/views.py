from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.db.models import Q

from .models import Movie

# Create your views here.
from django.http import HttpResponse

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'main/detail.html', {'movie': movie})

def index(request):
    if(request.GET.get('submitMovie')):
        search_query = request.GET.get('search_box', None)
        print(search_query)
        results = Movie.objects.filter(Q(name__icontains=search_query))
        print("search results:", results)
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'main/index.html', context)
