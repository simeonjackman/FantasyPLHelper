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
?goals_scored={goals}
?assists={assists}
?sort_by={key}
?show={key1,key2,...}
ex: {host}/players?sort_by=assists&name=f&show=first_name,second_name,goals_scored&min_cost=80
```

### /teams
Getter utility with basic filters for teams.
```
?name={name}
?id={id}

?strength={strength}
?max_strength={max_strength}
?min_strength={min_strength}

?strength_overall_home={strength_overall_home}
?max_strength_overall_home={max_strength_overall_home}
?min_strength_overall_home={min_strength_overall_home}

?strength_overall_away={strength_overall_away}
?max_strength_overall_away={max_strength_overall_away}
?min_strength_overall_away={min_strength_overall_away}

?strength_attack_home={strength_attack_home}
?max_strength_attack_home={max_strength_attack_home}
?min_strength_attack_home={min_strength_attack_home}

?strength_attack_away={strength_attack_away}
?max_strength_attack_away={max_strength_attack_away}
?min_strength_attack_away={min_strength_attack_away}

?strength_defence_home={strength_defence_home}
?max_strength_defence_home={max_strength_defence_home}
?min_strength_defence_home={min_strength_defence_home}

?strength_defence_away={strength_defence_away}
?max_strength_defence_away={max_strength_defence_away}
?min_strength_defence_away={min_strength_defence_away}

?show={key1,key2,...}
?sort_by={key}
ex: {host}/teams?name=team_name
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
?id={id}
?from={id}
?until={id}
?is_previous={y/n}
?is_current{y/n}
?is_next={y/n}
?finished={y/n}
?data_checked={y/n}
?deadline_after={YYYY-MM-DDZHH:MM:SS}
?show={key1,key2,...}
ex: {host}/events?from=10&until=20&finished=false&show=name,id,deadline_time
```

