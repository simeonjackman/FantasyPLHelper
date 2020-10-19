import requests
import pandas as pd
import numpy as np
import json

# this function call the fantasypl api and caches the data
# should be called before running the api
def data():
    print("calling fantasy PL api /bootstrap-static")
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/' # api url
    raw_response = requests.get(url) 								# call api
    response = raw_response.json()									# gets dict from reponse object

    # want to cache each entry in the response for clarity and readability
    print("caching data")
    for key in response.keys():
        with open("/tmp/{}.json".format(key), "w") as outfile: 
            # Serializing json  
            json_object = json.dumps(response[key], indent = 4) 
            outfile.write(json_object) 
            print("{} done".format(key))   


# this function call the fantasypl api and caches the data
# should be called before running the api
def fixtures():
    print("calling fantasy PL api /fixtures")
    url = 'https://fantasy.premierleague.com/api/fixtures/' # api url
    raw_response = requests.get(url) 								# call api
    response = raw_response.json()									# gets dict from reponse object


    # want to cache each entry in the response for clarity and readability
    print("caching data")
    with open("/tmp/fixtures.json", "w") as outfile: 
        # Serializing json  
        json_object = json.dumps(response, indent = 4) 
        outfile.write(json_object) 
        print("fixtures done")   