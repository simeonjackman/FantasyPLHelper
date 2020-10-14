import flask
from get_data import get_data

get_data()
app = flask.Flask(__name__)
app.config["DEBUG"] = True


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

    
    

if __name__ == "__main__":
    # running with host="0.0.0.0" makes the localhost visible from
    # outside of the docker container
    app.run(debug=True, host="0.0.0.0")