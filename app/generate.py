from flask import Flask,jsonify
import requests
import simplejson
import json

app = Flask(__name__)

def calcLongLat(data):
    for(int i = 1; i <6; i++):
        string = location + i #location1 field in json
        loc = data[string] #get from json address
        uri = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc + "&key=AIzaSyBHMScNZ7yXQ2PJ-yFkf4qmc7qQuzAQQWM"
        try:
            uResponse = requests.get(uri)
        except requests.ConnectionError:
           return "Connection Error"
        Jresponse = uResponse.text
        google = json.loads(Jresponse)
        

    displayName = data['items'][0]['display_name']# <-- The display name
    reputation = data['items'][0]['reputation']# <-- The reputation


    location1_ll =

def calcUberWalking (google_longlat):
