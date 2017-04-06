#
# This file handles communication with apple api.
#

# Sample API call:
# https://itunes.apple.com/search?parameterkeyvalue

import requests
import json


def apple_search_for_movie(movie_name):
    search = tmdb.Search()
    if movie_name == "":
        return []
    results = search.movie(query=movie_name)["results"]
    top_three = results[:3]
    return top_three
