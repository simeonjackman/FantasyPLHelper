import json
import requests

from .utils import str2bool

def load(args):
    print(args)

    with open('/tmp/fixtures.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)

    # finished fixtures
    if args.get('finished') is not None:
        filter_is_finished = str2bool(args.get('finished', default='', type=str))
        print('filtering for finished {}'.format(filter_is_finished))
        json_object = list(filter(lambda x: x['finished'] == filter_is_finished, json_object))

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