from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.db.models import Q
from .tmdb import search_for_movie
from .models import Movie

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def detail(request, movie_id):
    if(request.GET.get('submitMovie')):
        movie_list = search_movie(request)
        context = {'movie_list': movie_list}
        return render(request, 'main/index.html', context)
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'main/detail.html', {'movie': movie})

def index(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    if(request.GET.get('submitMovie')):
        movie_list = search_movie(request)
        context = {'movie_list': movie_list}
        return render(request, 'main/index.html', context)
    return render(request, 'main/index.html', context)

def search_movie(request):
    search_query = request.GET.get('search_box', None)
    movie_list = Movie.objects.filter(Q(name__icontains=search_query))
    if len(movie_list) == 0:
        m = Movie(name=search_query)
        m.save()
        movie_list = Movie.objects.filter(Q(name__icontains=search_query))
    return movie_list
