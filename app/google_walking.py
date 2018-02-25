import urllib, json

#given the starting and ending longitude and latitude
#returns the distance in miles and time in seconds
def getTimeAndDistance(startLong,startLat,endLong,endLat):
    #using the google API to get a JSON file of data
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + str(startLong) + '%2C' + str(startLat) + '&destinations=' + str(endLong) + '%2C' + str(endLat) +'&mode=walking&key=AIzaSyBHMScNZ7yXQ2PJ-yFkf4qmc7qQuzAQQWM'
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    #get Time in seconds
    first_JSon = data.get('rows')
    json_time_and_distance = first_JSon[0].get('elements')
    time = json_time_and_distance[0].get('duration').get('value')

    #get Distance in miles
    distance = json_time_and_distance[0].get('distance').get('text')
    distance = str(distance)

    #changing the distance to an int
    distance = distance[:-3]
    distance = float(distance)

    return distance, time;


print getTimeAndDistance(40.6655101,-73.89188969999998,40.6905615,-73.9976592)
