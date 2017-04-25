#
# This file handles communication with apple api.
#

# Sample API call:
# https://itunes.apple.com/search?media=movie&limit=1&term=terminator

import json
import requests

BASE_URL = "https://itunes.apple.com/search"

def apple_search(term):
    querystring = {"media":"movie","limit":"1","term":term}
    response = requests.request("GET", BASE_URL, params=querystring)
    data = json.loads(response.text)
    
    if data['resultCount'] == 1:
        result = data['results'][0]
        try:
            price = result['trackPrice']
            url = result['trackViewUrl']
        except KeyError:
            print("Call to apple API failed")
        return (price, url)
    else:
        # we don't have any results for apple
        return (0.00, "none")