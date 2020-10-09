# FantasyPLHelper
Helper for fantasy pl transfers


## Installation and Running

* Install dependencies in virtualenv: 
```
pipenv install
```

* Run virtualenv: 
```
source env/bin/activate
```


* Run install dependencies in virtualenv: 
```
pip3 install -r requirements.txt
```

* Run server in virtualenv: 
```
python3 main.py
```

## Running with Docker

Make sure you have the docker toolbox installed.

* Start by building the container:
```bash
make build
```

* Run the container:
```
make run
```

* Check whether your container is running:
```
docker ps
> CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS              PORTS                    NAMES
> e67904e80b84        fantasy_pl_helper:latest   "python main.py"    1 second ago        Up 1 second         0.0.0.0:5000->5000/tcp   fantasy_docker
``

* Test the application on localhost.

* Stop the docker container
```
make stop
```

* Clean up
```
make clean
```





# API DOC

## /players
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
