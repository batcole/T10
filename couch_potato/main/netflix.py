##http://netflixroulette.net/api/api.php?title=Attack%20on%20titan

import requests
import json

def find_netflix(term):
    url = "http://netflixroulette.net/api/api.php"
    querystring = {"title": term}
    response = requests.request("GET", url, params=querystring)
    return(response.text)