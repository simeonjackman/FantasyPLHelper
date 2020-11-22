import json
import flask
from flask_cors import CORS
from load import load
load.data()
load.fixtures()
load.top_squads(top_k=50)
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app) # This will enable CORS for all routes


# routes
@app.route('/', methods=['GET'])
def home():
    return "<h1>this should not be a server rendered webpage</h1>"

# call /players to get all players
from dataloader import players
@app.route('/players', methods=['GET'])
def show_players():   
    # pass get url args for filtering
    return players.load(flask.request.args)

# call /teams to get all teams
from dataloader import teams
@app.route('/teams', methods=['GET'])
def show_teams():   
    # pass get url args for filtering
    return teams.load(flask.request.args)

# call /element-types to get all event types
from dataloader import element_types
@app.route('/element-types', methods=['GET'])
def show_element_types():   
    # pass get url args for filtering
    return element_types.load(flask.request.args)

# call /events to get all event types
from dataloader import events
@app.route('/events', methods=['GET'])
def show_events():   
    # pass get url args for filtering
    return events.load(flask.request.args)

# call /fixtures to get all fixtures
from dataloader import fixtures
@app.route('/fixtures', methods=['GET'])
def show_fixtures():
    # pass get url args for filtering
    return fixtures.load(flask.request.args)

# call /top_player_picks to get the picks from top players
from dataloader import top_player_picks
@app.route('/top_player_picks', methods=['GET'])
def show_top_player_picks():
    # pass get url args for filtering
    return top_player_picks.load(flask.request.args)

# call /recommend to get a recommendation from collaborative filtering
from recommender import build_recommender_system_from_loader
from recommender import parse_args, parse_response
rec_system = build_recommender_system_from_loader(top_player_picks)
@app.route('/player2player', methods=['GET'])
def player2player():
    # who do the top users pick alongside player with id=X?
    player_id, top = parse_args(flask.request.args)
    ids, values = rec_system.item_to_item(player_id, top=top)
    return parse_response(ids, values)


if __name__ == "__main__":
    # running with host="0.0.0.0" makes the localhost visible from
    # outside of the docker container
    app.run(debug=True, host="0.0.0.0")