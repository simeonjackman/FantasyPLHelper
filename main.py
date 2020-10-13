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

# call /element-types to get all event types
from dataloader import element_types
@app.route('/element-types', methods=['GET'])
def show_element_types():   
    # pass get url args for filtering
    return element_types.load(flask.request.args)

    

if __name__ == "__main__":
    app.run(debug=True)