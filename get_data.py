import requests
import pandas as pd
import numpy as np
import json

url = 'https://fantasy.premierleague.com/api/bootstrap-static/' # api url
raw_response = requests.get(url) 								# call api
reponse = raw_response.json()									# gets dict from reponse object

# want to cache each entry in the response for clarity and readability
for key in reponse.keys():
    with open("./cached-data/{}.json".format(key), "w") as outfile: 
        # Serializing json  
        json_object = json.dumps(reponse[key], indent = 4) 
        outfile.write(json_object) 