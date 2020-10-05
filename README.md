# FantasyPLHelper
Helper for fantasy pl transfers

Install dependencies in virtualenv: 
```
pipenv install
```

Run through virtualenv: 
```
pipenv run python3 server.py
```


# API DOC

## /players
```
?name={name}
?min_cost={cost}
?max_cost={cost}
?goals_scored{goals}
?assists{assists}
```
