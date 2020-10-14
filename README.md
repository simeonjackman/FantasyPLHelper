# FantasyPLHelper
A helper for the Premier League Fantasy Football game. 


## Installation

### Default
Install dependencies in virtualenv:
```
pipenv install
```

Run virtualenv: 
```
source env/bin/activate
```
Install dependencies in virtualenv: 
```
pip3 install -r requirements.txt
```
Run server in virtualenv: 
```
python3 main.py
```

### Docker

Make sure you have the docker toolbox installed.

Start by building the container:
```
make build
```
Run the container:
```
make run
```
Check whether your container is running:
```
docker ps
> CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS              PORTS                    NAMES
> e67904e80b84        fantasy_pl_helper:latest   "python main.py"    1 second ago        Up 1 second         0.0.0.0:5000->5000/tcp   fantasy_docker
```
Test the application on localhost.

Stop the docker container:
```
make stop
```

Clean up tangling docker images and caches:
```
make clean
```


## API Documentation

### /players
Getter utility with basic filters for players.
```
?name={name}
?min_cost={cost}
?max_cost={cost}
?goals_scored{goals}
?assists{assists}
?sort_by{key}
?show{key1,key2,...}
ex: {host}/players?sort_by=assists&name=f&show=first_name,second_name,goals_scored&min_cost=80
```

### /teams
Getter utility with basic filters for teams.
```
?name={name}
?show={key1,key2,...}
ex: {host}/teams?
name=team_name
```

### /element-types
Getter utility with basic filters for element types.
```
?show={key1,key2,...}
ex:
```

### /events
Getter utility with basic filters for events.
```
?show={key1,key2,...}
ex:
```

