from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import json

session = Session(server_token="wJFmlljkrczBkDB7k9_CPOxhgmX2KaiLd-bxlQPb")
client = UberRidesClient(session)

#returns two outputs: duration time in seconds and cost in dollars
def findCostAndTime (startLat,startLong,endLat,endLong,seat = 1):
    response = client.get_price_estimates(
    start_latitude= startLat,
    start_longitude= startLong,
    end_latitude= endLat,
    end_longitude= endLong,
    seat_count=2
    )

    #list of all the diff possibilities of ubers
    estimate = response.json.get('prices')

    #ubers select option
    first_JSon = estimate[0]

    #duration time in seconds
    #estimate cost is in dollars
    duration_time = first_JSon['duration']
    estimate_cost = first_JSon['high_estimate']

    return duration_time, estimate_cost;

#test
returnedDuration, returnedTime = findCostAndTime(37.770,-122.411,37.791,-122.405)
print returnedTime
print returnedDuration

# walking https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101%2C-73.89188969999998&destinations=40.6905615%2C-73.9976592&mode=walking&key=AIzaSyBHMScNZ7yXQ2PJ-yFkf4qmc7qQuzAQQWM
