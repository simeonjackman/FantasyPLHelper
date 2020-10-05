import json
import requests

def load(args):
	print(args)
	
	with open('/tmp/elements.json', 'r') as openfile: 
		# Reading from json file 
		json_object = json.load(openfile)

	# filter name
	if args.get('name') is not None and args.get('name') != '':
		filter_name = args.get('name')
		print("filtering name for {}".format(filter_name))
		json_object = list(filter(lambda x:
			filter_name.lower() in x['first_name'].lower() or 
			filter_name.lower() in x['second_name'].lower() or
			filter_name.lower() in x['web_name'].lower(), json_object))


	return json.dumps(json_object)