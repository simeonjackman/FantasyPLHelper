import json
import requests

from .utils import str2bool, correct_time_format

def load(args):
    print(args)

    with open('/tmp/fixtures.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)

    # filter id
    if args.get('id') is not None and args.get('id') != '':
        filter_id = args.get('id', default='', type=int)
        print('filtering id for {}'.format(filter_id))
        json_object = list(filter(lambda x:
            filter_id == int(x['id']), json_object))

    # finished fixtures
    if args.get('finished') is not None:
        filter_is_finished = str2bool(args.get('finished', default='', type=str))
        print('filtering for finished {}'.format(filter_is_finished))
        json_object = list(filter(lambda x: x['finished'] == filter_is_finished, json_object))

    # kickoff time after
    if args.get('kickoff_after') is not None and args.get('kickoff_after') != '':
        filter_kickoff = args.get('kickoff_after', default='', type=str)
        if correct_time_format(filter_kickoff):
            print('filtering for kickoff after {}'.format(filter_kickoff))
            json_object = list(filter(
                lambda x: x['kickoff_time'] is not None 
                and x['kickoff_time'] > filter_kickoff, json_object))

    # filter home team
    if args.get('team_h') is not None and args.get('team_h') != '':
        filter_team = args.get('team_h', default='', type=int)
        print('filtering home teams for {}'.format(filter_team))
        json_object = list(filter(
            lambda x: filter_team == x['team_h'], json_object))

    # filter away team
    if args.get('team_a') is not None and args.get('team_a') != '':
        filter_team = args.get('team_a', default='', type=int)
        print('filtering away teams for {}'.format(filter_team))
        json_object = list(filter(
            lambda x: filter_team == x['team_a'], json_object))

    # filter team playing
    if args.get('team') is not None and args.get('team') != '':
        filter_team = args.get('team', default='', type=int)
        print('filtering teams for {}'.format(filter_team))
        json_object = list(filter(
            lambda x: filter_team in [x['team_h'], x['team_a']], json_object))

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