import json


def get():
    """Calculates the scorer points for all players.

    """

    # load player data
    with open('/tmp/elements.json', 'r') as openfile: 
        # Reading from json file 
        json_object = json.load(openfile)

    # calculate scorer points
    points = map(lambda x: x['goals_scored'] + x['assists'], json_object)

    # build result
    result = []
    for player, point in zip(json_object, points):
        result.append({
            'player': player,
            'score': point,
        })

    # return player summary
    return result

