#
# This file handles communication with tmdb api.
#

# Sample API call:
# https://api.themoviedb.org/3/movie/<movie_number>?api_key=<pkey>

import http.client
import json

# In this string, %s will be replaced by the movie number.
BASE_URL = '/3/movie/%s?api_key=74b5f1b300deec307cbe4df5228627a6'


def get_movie(movie_number):
    connection = http.client.HTTPSConnection("api.themoviedb.org")
    connection.request("GET", BASE_URL % movie_number)
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    return data
