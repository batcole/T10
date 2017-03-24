#
# This file handles communication with tmdb api.
#

# Sample API call:
# https://api.themoviedb.org/3/movie/<movie_number>?api_key=<pkey>

import requests
import json
import tmdbsimple as tmdb
from .keys import API_KEY
tmdb.API_KEY = API_KEY

def search_for_movie(movie_name):
    search = tmdb.Search()
    if movie_name == "":
        return []
    results = search.movie(query=movie_name)["results"]
    top_three = results[:3]
    return top_three
