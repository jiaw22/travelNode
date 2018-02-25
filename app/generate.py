# from flask import Flask,jsonify
# import requests
# import simplejson
# import json
# from uber import *
# from google_walking import *
# from min_spanning_tree import *
#
# def generateTimeParam(data, addr):
#     times = []
#     i = 1
#     while i < len(addr)+1:
#         ts = "location_time" + str(i) #location1 field in json
#         time = data[ts]
#         loc = addr[i-1][0] #get from json address
#         tup = (loc, time)
#         times.append(tup)
#         i = i + 1
#     return times
#
# def calcLongLat(data):
#     loc_data = []
#     i = 1
#     while i < 6:
#         string = "location" + str(i) #location1 field in json
#         print string
#         ts = "location_time" + str(i) #location1 field in json
#         loc = data[string] #get from json address
#         if loc: #if location was entered
#             uri = "https://maps.googleapis.com/maps/api/geocode/json?address=" + loc + "&key=AIzaSyBHMScNZ7yXQ2PJ-yFkf4qmc7qQuzAQQWM"
#             try:
#                 uResponse = requests.get(uri)
#             except requests.ConnectionError:
#                return "Connection Error"
#             Jresponse = uResponse.text
#             # print Jresponse
#             google = json.loads(Jresponse)
#             # print google
#             addr = google["results"][0]["formatted_address"]
#             lat = google["results"][0]["geometry"]["location"]["lat"]
#             lng = google["results"][0]["geometry"]["location"]["lng"]
#             loc = (addr, lat, lng)
#             loc_data.append(loc)
#         i = i + 1
#     return loc_data
#
# def calcUberWalking (google_longlat):
#     ret = []
#     i = 0
#     while i < len(google_longlat):
#         j = i + 1
#         while j < len(google_longlat):
#             u = findCostAndTime(google_longlat[i][1], google_longlat[i][2], google_longlat[j][1], google_longlat[j][2]) # cost,time
#             w= getTimeAndDistance(google_longlat[i][1], google_longlat[i][2], google_longlat[j][1], google_longlat[j][2]) # time, cost
#             tup = (google_longlat[i][0], google_longlat[j][0], u[0], u[1], w[1], w[0]) # addr1, addr2, u_cost, u_time, w_time, w_dist
#             ret.append(tup)
#             j = j + 1
#         i = i + 1
#     return ret
#
# def callCaroline(orgdata, data1, time):
#     try:
#         if data["personal"]:
#             own_vehicle = "yes"
#         else:
#             own_vehicle = "no"
#     except KeyError:
#          own_vehicle = "no"
#     max_time = data["timelimit"]
#     activity_level = data["active"]
#     results = construct_whole(data1, time, own_vehicle, max_time, activity_level)
#     return results
#
#
# string = """{
#   "active": "50",
#   "location1": "Klarman Hall, East Avenue, Ithaca, NY, USA",
#   "location2": "111 Dryden Road, Ithaca, NY, USA",
#   "location3": "",
#   "location4": "",
#   "location5": "",
#   "location_time1": "50",
#   "location_time2": "50",
#   "location_time3": "",
#   "location_time4": "",
#   "location_time5": "",
#   "timelimit": "4"
# }"""
# # data = json.loads(string)
# # ll = calcLongLat(data)
# # times = generateTimeParam(data, ll)
# # u_w = calcUberWalking(ll)
# # callCaroline(data, u_w, times)
# # callCaroline(data, u_w, times)
