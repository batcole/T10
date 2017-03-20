from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question
from .tmdb import *

# Create your views here.
from django.http import HttpResponse

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'main/index.html', context)

def show_movie(request, movie_number):
    # TODO implement this method to properly get data. wire it up to some
    # urls on a page, with templates.
    data = tmdb.get_movie(movie_number)
    context = {}
    return render(request, 'main/movie_template.html', context)
