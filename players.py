import json

def load_players():
	with open('cached-data/elements.json', 'r') as openfile: 
	
		# Reading from json file 
		json_object = json.load(openfile)
	return json.dumps(json_object)