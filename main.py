import json
import flask
from flask_cors import CORS
from load import load


N_TOP_USERS = 50 * 1
def load_data():
    load.data()
    load.fixtures()
    load.top_squads(top_k=N_TOP_USERS)


load_data()
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
@app.route('/top-player-picks', methods=['GET'])
def show_top_player_picks():
    # pass get url args for filtering
    return top_player_picks.load(flask.request.args)

# call /player-to-player/player_id
from routes import player_to_player
rec_system = player_to_player._build_recommender_system(top_player_picks)
@app.route('/player-to-player/<player_id>', methods=['GET'])
def player_to_player_(player_id):
    # who do the top users pick alongside player with id=X?
    return player_to_player.get(player_id, flask.request.args, rec_system)

# call /player-summary/player_id to get a player summary
from routes import player_summary
@app.route('/player-summary/<player_id>', methods=['GET'])
def player_summary_(player_id):
    # pass player_id and url args
    return player_summary.get(player_id, flask.request.args)

# call /player-score/score to get the score for a player
from routes import player_score
@app.route('/score/<score>', methods=['GET'])
def player_score_(score):
    # pass score and args
    return player_score.get(score, flask.request.args)


if __name__ == "__main__":
    # running with host="0.0.0.0" makes the localhost visible from
    # outside of the docker container
    app.run(debug=True, host="0.0.0.0")