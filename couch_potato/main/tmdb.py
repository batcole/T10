#
# This file handles communication with tmdb api.
#

# Sample API call:
# https://api.themoviedb.org/3/movie/<movie_number>?api_key=<pkey>

import requests
import json

# In these strings, %s will be replaced by the movie number.
# for example, "test %s" % "injected value" will result in "test injected value"

BASE_URL = "https://api.themoviedb.org/3"
ID_URL = BASE_URL + "/movie/%s"
SEARCH_URL = BASE_URL + "/search/movie"

def movie_data_by_id(movie_id):
    params = {"api_key":"74b5f1b300deec307cbe4df5228627a6"}

    response = requests.request("GET", ID_URL % movie_id, params=params)
    if response.status_code != 200:
        return []
    
    data = json.loads(response.text)
    return data

def search_for_movie(movie_name):
    params = {"api_key":"74b5f1b300deec307cbe4df5228627a6",
              "query": movie_name
              }
    
    response = requests.request("GET", SEARCH_URL, params=params)
    if response.status_code != 200:
        return []

    results = json.loads(response.text)["results"]
    top_three = results[:3]
    return top_three
