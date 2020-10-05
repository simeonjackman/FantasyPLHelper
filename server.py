import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>FantasyPLHelper</h1><p>Rip liverpool</p>"

app.run()