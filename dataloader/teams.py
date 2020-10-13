import json
import requests

def load(args):
	print(args)
	
	with open('/tmp/teams.json', 'r') as openfile: 
		# Reading from json file 
		json_object = json.load(openfile)

	# filter name
	if args.get('name') is not None and args.get('name') != '':
		filter_name = args.get('name', default='', type=str)
		print("filtering name for {}".format(filter_name))
		json_object = list(filter(lambda x:
			filter_name.lower() in x['name'].lower(),json_object))

	# show fields
	if args.get('show') is not None and args.get('show') != '' and len(json_object) > 0:
		show = args.get('show', default='', type=str)
		show_keys = show.split(',')
		show_keys = list(filter(lambda key: key in json_object[0], show_keys)) # remove invalid keys
		print("showing >= {}".format(show_keys))
		json_object = list(map( lambda object: { key: object[key] for key in show_keys }, json_object))

	# check empty
	if len(json_object) == 0:
		return '[]'
	return json.dumps(json_object)