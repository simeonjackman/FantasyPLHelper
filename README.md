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
