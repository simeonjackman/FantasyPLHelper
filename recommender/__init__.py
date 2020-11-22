import json
from typing import List
from simple_rec import CollaborativeFilter


def build_recommender_system_from_loader(loader, k=8):
    """Loads the top user's picks and builds a collaborative filter from them.

    The rows denote the top users and the columns denote the selected players.

    """
    from werkzeug.datastructures import ImmutableMultiDict

    # load the top player data
    args = ImmutableMultiDict([('show', 'picks')])
    data = loader.load(args)
    data = json.loads(data)

    # build the collaborative filter
    users, items, observations = [], [], []
    for user, data_item in enumerate(data):
        for player in data_item['picks']:
            users.append(user)              # user id
            items.append(player['element']) # player id
            observations.append(1.)         # observed

    collab_filter = CollaborativeFilter(users, items, observations)
    collab_filter.fit(k=k)

    return collab_filter



def parse_args(args):
    """Parses the arguments and converts them to a suitable format.

    """
    player_id, top = 1, 1

    # get player id
    if args.get('id') is not None and args.get('id') != '':
        player_id = args.get('id', default='', type=int)

    # get top 
    if args.get('top') is not None and args.get('top') != '':
        top = args.get('top', default='', type=int)

    return player_id, top


def parse_response(ids: List[int], values: List[float]):
    """Takes the return values from the recommender system and converts to json.

    """
    # handle special cases
    if len(ids) == 0 or len(ids) != len(values):
        return '[]'

    # build dictionary and dump as json
    response = []
    for id_, value in zip(ids, values):
        response.append({
            'id': int(id_),
            'agreement': float(value)
        })

    return json.dumps(response)
 