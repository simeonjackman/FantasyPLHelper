import json
import requests

from .utils import str2bool
from .utils import correct_deadline_time_format


def load(args):
	print(args)
	
	with open('/tmp/events.json', 'r') as openfile: 
		# Reading from json file 
		json_object = json.load(openfile)

	# filter id
	if args.get('id') is not None and args.get('id') != '':
		filter_id = args.get('id', default='', type=int)
		print('filtering id for {}'.format(filter_id))
		json_object = list(filter(lambda x:
			filter_id == int(x['id']), json_object))

	# filter ids from
	if args.get('from') is not None and args.get('from') != '':
		filter_from = args.get('from', default='', type=int)
		print('filtering id for {}'.format(filter_from))
		json_object = list(filter(lambda x:
			filter_from <= int(x['id']), json_object))

	# filter ids until
	if args.get('until') is not None and args.get('until') != '':
		filter_until = args.get('until', default='', type=int)
		print('filtering id for {}'.format(filter_until))
		json_object = list(filter(lambda x:
			filter_until >= int(x['id']), json_object))

	# previous gameweek
	if args.get('is_previous') is not None:
		filter_is_previous = str2bool(args.get('is_previous', default='', type=str))
		print('filtering for is_previous {}'.format(filter_is_previous))
		json_object = list(filter(lambda x: x['is_previous'] == filter_is_previous, json_object))

	# current gameweek
	if args.get('is_current') is not None:
		filter_is_current = str2bool(args.get('is_current', default='', type=str))
		print('filtering for is_current {}'.format(filter_is_current))
		json_object = list(filter(lambda x: x['is_current'] == filter_is_current, json_object))

	# next gameweek
	if args.get('is_next') is not None:
		filter_is_next = str2bool(args.get('is_next', default='', type=str))
		print('filtering for is_next {}'.format(filter_is_next))
		json_object = list(filter(lambda x: x['is_next'] == filter_is_next, json_object))

	# finished gameweeks
	if args.get('finished') is not None:
		filter_is_finished = str2bool(args.get('finished', default='', type=str))
		print('filtering for finished {}'.format(filter_is_finished))
		json_object = list(filter(lambda x: x['finished'] == filter_is_finished, json_object))

	# data checked gameweeks
	if args.get('data_checked') is not None:
		filter_is_data_checked = str2bool(args.get('data_checked', default='', type=str))
		print('filtering for data checked {}'.format(filter_is_data_checked))
		json_object = list(filter(lambda x: x['data_checked'] == filter_is_data_checked, json_object))

	# filter deadline time
	if args.get('deadline_after') is not None and args.get('deadline_after') != '':
		filter_deadline = args.get('deadline_after', default='', type=str)
		if correct_deadline_time_format(filter_deadline):
			print('filtering for deadline after {}'.format(filter_deadline))
			json_object = list(filter(lambda x: x['deadline_time'] > filter_deadline, json_object))

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