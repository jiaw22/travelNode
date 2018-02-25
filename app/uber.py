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
    seat_count=1
    )

    #list of all the diff possibilities of ubers
    estimate = response.json.get('prices')

    #ubers select option
    first_JSon = estimate[0]

    #duration time in seconds
    #estimate cost is in dollars
    duration_time = first_JSon['duration']
    estimate_cost = first_JSon['high_estimate']

    return (duration_time, estimate_cost)

# print(findCostAndTime(37.770,-122.411,37.791,-122.405))
#
# # def main():
# #     res = findCostAndTime(37.770,-122.411,37.791,-122.405)
# #     print(res)
# #
# # if __name__ == '__main__':
# #     if len(sys.argv) > 1:
# #         main()
#
# # stuff = findCostAndTime(37.770,-122.411,37.791,-122.405)
# # print stuff
#
# client.get_price_estimates(start_latitude= 37.770,start_longitude= -122.411,end_latitude= 37.791,end_longitude= -122.405,seat_count=1
# )
# walking https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101%2C-73.89188969999998&destinations=40.6905615%2C-73.9976592&mode=walking&key=AIzaSyBHMScNZ7yXQ2PJ-yFkf4qmc7qQuzAQQWM
