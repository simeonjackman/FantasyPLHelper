import requests
import pandas as pd
import numpy as np
import json
import os

# this function calls the fantasypl api and caches the data
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


# this function calls the fantasypl api and caches the data
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


# this function calls the fantasypl api and caches the data
# should be called before running the api
N_OVERALL_EVENTS = 38
ENTRIES_PER_PAGE = 50
def top_squads(league: int = 314,
               top_k: int = 50):

    base_url = "https://fantasy.premierleague.com/api/"

    # step 1: find the top players
    top_player_ids = []
    for i in range(top_k // ENTRIES_PER_PAGE):
        # load standings
        url = f"{base_url}leagues-classic/{league}/standings/?page_standings={i+1}"
        raw_response = requests.get(url)
        response = raw_response.json()

        # store best players
        for result in response['standings']['results']:
            top_player_ids.append(result['entry'])

    assert len(top_player_ids) == top_k

    basepath = "/tmp/top_player_picks/"
    os.makedirs(basepath, exist_ok=True)

    # step 2: get latest picks for best player
    # (use this to get the latest available event)
    event, event_ = None, N_OVERALL_EVENTS
    while event is None and event_ > 0:
        url = f"{base_url}entry/{top_player_ids[0]}/event/{event_}/picks/"
        raw_response = requests.get(url)
        if raw_response.status_code == 200:
            response = raw_response.json()
            event = event_
            break
        event_ = event_ - 1
    
    print("caching top player picks")
    path = os.path.join(basepath, "top_player_picks_1.json")
    with open(path, "w") as outfile: 
        # Serializing json  
        json_object = json.dumps(response, indent = 4) 
        outfile.write(json_object)

    # step 3: get latest picks of all top players
    for i in range(1, top_k):
        url = f"{base_url}entry/{top_player_ids[i]}/event/{event}/picks/"
        raw_response = requests.get(url)
        if raw_response.status_code != 200:
            continue
        response = raw_response.json()
        
        print(f"caching top player {i+1} picks")
        path = os.path.join(basepath, f"top_player_picks_{i+1}.json")
        with open(path, "w") as outfile: 
            # Serializing json  
            json_object = json.dumps(response, indent = 4) 
            outfile.write(json_object)
    
    print("top player picks done")