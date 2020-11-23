import json
from . import scorer_points


def get(score, args):
    """Returns the selected score for each selected player.

    """

    # get score
    if score is None or score == '':
        return '[]'
    elif score == 'scorer-points':
        result = scorer_points.get()

    # sort in descending order
    result = sorted(result, key=lambda x: x['score'])[::-1]

    # filter by id
    if args.get('id') is not None and args.get('id') != '':
        filter_id = args.get('id', default='', type=int)
        print("filtering id for {}".format(filter_id))
        result = list(filter(lambda x: filter_id == x['player']['id'], result))

    # TODO: add more filters

    return json.dumps(result)