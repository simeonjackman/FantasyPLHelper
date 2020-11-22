import os
import json
import requests

def load(args):
    print(args)

    json_object = []
    for filename in os.listdir('/tmp/top_player_picks/'):
        path = os.path.join('/tmp/top_player_picks/', filename)
        print(path)
        with open(path, 'r') as openfile:
            # Reading from json file
            json_object.append(json.load(openfile))

    # rank
    if args.get('rank') is not None and args.get('rank') != '' and len(json_object) > 0:
        filter_rank = args.get('rank', default='', type=int) - 1
        print('filtering rank for {}'.format(filter_rank))
        json_object = [json_object[filter_rank]]

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