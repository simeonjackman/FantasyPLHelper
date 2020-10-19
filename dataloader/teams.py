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
			filter_name.lower() == x['name'].lower() or
			filter_name.lower() == x['short_name'].lower(), json_object))

	# id
	if args.get('id') is not None and args.get('id') != '':
		filter_id = args.get('id', default='', type=int)
		print('filtering id for {}'.format(filter_id))
		json_object = list(filter(lambda x: filter_id == x['id'], json_object))

	# strength
	if args.get('strength') is not None and args.get('strength') != '':
		filter_strength = args.get('strength', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength'], json_object))

	# max strength
	if args.get('max_strength') is not None and args.get('max_strength') != '':
		filter_strength = args.get('max_strength', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength'], json_object))

	# min strength
	if args.get('min_strength') is not None and args.get('min_strength') != '':
		filter_strength = args.get('min_strength', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength'], json_object))

	# strength overall home
	if args.get('strength_overall_home') is not None and args.get('strength_overall_home') != '':
		filter_strength = args.get('strength_overall_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength_overall_home'], json_object))

	# max strength overall home
	if args.get('max_strength_overall_home') is not None and args.get('max_strength_overall_home') != '':
		filter_strength = args.get('max_strength_overall_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength_overall_home'], json_object))

	# min strength overall home
	if args.get('min_strength_overall_home') is not None and args.get('min_strength_overall_home') != '':
		filter_strength = args.get('min_strength_overall_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength_overall_home'], json_object))

	# strength overall away
	if args.get('strength_overall_away') is not None and args.get('strength_overall_away') != '':
		filter_strength = args.get('"strength_overall_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength_overall_away'], json_object))

	# max strength overall away
	if args.get('max_strength_overall_away') is not None and args.get('max_strength_overall_away') != '':
		filter_strength = args.get('max_strength_overall_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength_overall_away'], json_object))

	# min strength overall away
	if args.get('min_strength_overall_away') is not None and args.get('min_strength_overall_away') != '':
		filter_strength = args.get('min_strength_overall_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength_overall_away'], json_object))

	# strength attack home
	if args.get('strength_attack_home') is not None and args.get('strength_attack_home') != '':
		filter_strength = args.get('strength_attack_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength_attack_home'], json_object))

	# max strength attack home
	if args.get('max_strength_attack_home') is not None and args.get('max_strength_attack_home') != '':
		filter_strength = args.get('max_strength_attack_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength_attack_home'], json_object))

	# min strength attack home
	if args.get('min_strength_attack_home') is not None and args.get('min_strength_attack_home') != '':
		filter_strength = args.get('min_strength_attack_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength_attack_home'], json_object))

	# strength attack away
	if args.get('strength_attack_away') is not None and args.get('strength_attack_away') != '':
		filter_strength = args.get('strength_attack_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength_attack_away'], json_object))

	# max strength attack away
	if args.get('max_strength_attack_away') is not None and args.get('max_strength_attack_away') != '':
		filter_strength = args.get('max_strength_attack_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength_attack_away'], json_object))

	# min strength attack away
	if args.get('min_strength_attack_away') is not None and args.get('min_strength_attack_away') != '':
		filter_strength = args.get('min_strength_attack_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength_attack_away'], json_object))

	# strength defence home
	if args.get('strength_defence_home') is not None and args.get('strength_defence_home') != '':
		filter_strength = args.get('strength_defence_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength_defence_home'], json_object))

	# max strength defence home
	if args.get('max_strength_defence_home') is not None and args.get('max_strength_defence_home') != '':
		filter_strength = args.get('max_strength_defence_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength_defence_home'], json_object))

	# min strength defence home
	if args.get('min_strength_defence_home') is not None and args.get('min_strength_defence_home') != '':
		filter_strength = args.get('min_strength_defence_home', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength_defence_home'], json_object))

	# strength defence away
	if args.get('strength_defence_away') is not None and args.get('strength_defence_away') != '':
		filter_strength = args.get('strength_defence_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength == x['strength_defence_away'], json_object))

	# max strength defence away
	if args.get('max_strength_defence_away') is not None and args.get('max_strength_defence_away') != '':
		filter_strength = args.get('max_strength_defence_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength >= x['strength_defence_away'], json_object))

	# min strength defence away
	if args.get('min_strength_defence_away') is not None and args.get('min_strength_defence_away') != '':
		filter_strength = args.get('min_strength_defence_away', default='', type=int)
		print('filtering strength for {}'.format(filter_strength))
		json_object = list(filter(lambda x: filter_strength <= x['strength_defence_away'], json_object))

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