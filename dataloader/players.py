import json
import requests

def load(args):
	print(args)

	return '[Hello World]'
	
	with open('/tmp/elements.json', 'r') as openfile: 
		# Reading from json file 
		json_object = json.load(openfile)

	# filter name
	if args.get('name') is not None and args.get('name') != '':
		filter_name = args.get('name', default='', type=str)
		print("filtering name for {}".format(filter_name))
		json_object = list(filter(lambda x:
			filter_name.lower() in x['first_name'].lower() or 
			filter_name.lower() in x['second_name'].lower() or
			filter_name.lower() in x['web_name'].lower(), json_object))

	# filter cost
	if args.get('min_cost') is not None and args.get('min_cost') != '':
		min_cost = args.get('min_cost', default=0, type=int)
		print("filtering cost > {}".format(min_cost))
		json_object = list(filter(lambda x: min_cost < x['now_cost'], json_object))
		
	if args.get('max_cost') is not None and args.get('max_cost') != '':
		max_cost = args.get('max_cost', default=200, type=int)
		print("filtering cost < {}".format(max_cost))
		json_object = list(filter(lambda x: max_cost > x['now_cost'], json_object))

	# filter goals
	if args.get('goals_scored') is not None and args.get('goals_scored') != '':
		goals_scored = args.get('goals_scored', default=0, type=int)
		print("filtering goals >= {}".format(goals_scored))
		json_object = list(filter(lambda x: goals_scored < x['goals_scored'], json_object))

	# filter assists
	if args.get('assists') is not None and args.get('assists') != '':
		assists = args.get('assists', default=0, type=int)
		print("filtering assists >= {}".format(assists))
		json_object = list(filter(lambda x: assists < x['assists'], json_object))

	# filter goals + assists
	if args.get('scorer_points') is not None and args.get('scorer_points') != '':
		scorer_points = args.get('scorer_points', default=0, type=int)
		print("filtering scorer points >= {}".format(scorer_points))
		json_object = list(filter(lambda x: scorer_points < x['assists'] + x['goals_scored'], json_object))

	# sort_by
	if args.get('sort_by') is not None and args.get('sort_by') != '' and len(json_object) > 0 and args.get('sort_by') in json_object[0]:
		sort_key = args.get('sort_by', default='', type=str)
		print("sorting by >= {}".format(sort_key))
		json_object = list(sorted(json_object, key = lambda i: (i[sort_key])))

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