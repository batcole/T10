#
# This file handles communication with tmdb api.
#

# Sample API call:
# https://api.themoviedb.org/3/movie/<movie_number>?api_key=<pkey>

import http.client
import json

# In these strings, %s will be replaced by the movie number.
BASE_URL = "api.themoviedb.org"
ID_URL = '/3/movie/%s?api_key=74b5f1b300deec307cbe4df5228627a6'
SEARCH_URL = "/3/search/movie?api_key=74b5f1b300deec307cbe4df5228627a6&query=%s"

def movie_data_by_id(movie_id):
    connection = http.client.HTTPSConnection(BASE_URL)
    connection.request("GET", ID_URL % movie_id)
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    return data

def search_for_movie(movie_name):
    connection = http.client.HTTPSConnection(BASE_URL)
    connection.request("GET", SEARCH_URL % movie_name)
    response = connection.getresponse()
    results = json.loads(response.read().decode("utf-8"))["results"]
    
    top_three = results[:3]
    return top_three
