import json


def get(player_id, args):
    """Returns a summary of the requested player.

    """

    # load player data
    with open('/tmp/elements.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)

    # find player with id
    json_object = list(filter(lambda x: int(player_id) == x['id'], json_object))
    if len(json_object) == 0:
        return '[]'

    # TODO: add more things to the summary

    # return player summary
    return json.dumps(json_object)
