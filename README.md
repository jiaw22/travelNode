# travelNode
Hack the Valley 2 - 2018
## Instalations
```
pip install -U pyopenssl
pip install uber_rides
pip install Flask
```
## To run app
export FLASK_APP=app.py
flask run
* if it warns you that port already in use, then run:
sudo lsof -t -i tcp:5000 | xargs kill -9


