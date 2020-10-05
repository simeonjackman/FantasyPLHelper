import requests
import pandas as pd
import numpy as np
import json

# this function call the fantasypl api and caches the data
# should be called before running the api
def get_data():
    print("calling fantasy PL api")
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/' # api url
    raw_response = requests.get(url) 								# call api
    reponse = raw_response.json()									# gets dict from reponse object

    # want to cache each entry in the response for clarity and readability
    print("caching data")
    for key in reponse.keys():
        with open("/tmp/{}.json".format(key), "w") as outfile: 
            # Serializing json  
            json_object = json.dumps(reponse[key], indent = 4) 
            outfile.write(json_object) 
            print("{} done".format(key))   