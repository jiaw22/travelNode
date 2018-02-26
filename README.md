# travelNode
Hack the Valley 2 - 2018
## Installations
```
pip install -U pyopenssl
pip install uber_rides
pip install Flask
```
## Running Application
```
export FLASK_APP=app.py
flask run
```
* if it warns you that port already in use, then run:
```
sudo lsof -t -i tcp:5000 | xargs kill -9
```

