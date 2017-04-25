#
# This file handles communication with netflix api.
#

# Sample API call:
# http://netflixroulette.net/api/api.php?title=Attack%20on%20titan

import json
import requests

BASE_URL = "http://netflixroulette.net/api/api.php"

def netflix_search(term):
    querystring = {"title":term}
    response = requests.request("GET", BASE_URL, params=querystring)
    data = json.loads(response.text)
    try:
        url = "https://www.netflix.com/title/" + str(data['show_id'])
        return url
    except KeyError:
        print("Unable to find movie on netflix API")
        return "none"
