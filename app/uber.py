from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import json

session = Session(server_token="wJFmlljkrczBkDB7k9_CPOxhgmX2KaiLd-bxlQPb")
client = UberRidesClient(session)

#hard-coded values but should be able to be changed
response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
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

print duration_time
print estimate_cost
