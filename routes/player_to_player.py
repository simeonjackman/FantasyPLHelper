import json
from simple_rec import CollaborativeFilter


def _build_recommender_system(loader, k=8):
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


def get(player_id, args, rec_system):
    """Queries a collaborative filter and returns nearest neighbors.

    """

    # load player data
    with open('/tmp/elements.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)

    # get additional arguments
    if args.get('top') is not None and args.get('top') != '':
        top = args.get('top', default='', type=int)
    else:
        top = 1

    # get recommendations from recommender system
    player_id = int(player_id)
    player_ids, agreements = rec_system.item_to_item(player_id, top=top)

    # find players
    json_object = list(filter(lambda x: x['id'] in player_ids, json_object))

    if len(json_object) == 0:
        return '[]'
    if len(json_object) != len(agreements):
        return '[]'

    # build return dictionary
    result = []
    for player, agreement in zip(json_object, agreements):
        result.append({
            'player': player,
            'agreement': agreement,
        })

    # return player summary
    return json.dumps(result)
