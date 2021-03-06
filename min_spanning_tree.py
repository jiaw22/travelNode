# Reference: Geeks for Geeks
# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys  # Library for INT_MAX

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        route = []
        print "Edge \tWeight"
        for i in range(1,self.V):
            print parent[i],"-",i,"\t",self.graph[i][ parent[i] ]
            route.append(parent[i])
        return route

    '''def getPath(self, parent):
        route = []
        #print "Edge \tWeight \tCost"
        for i in range(1,self.V):
            route.append(parent[i])
        return route
    '''
    # A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxint

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph represented using
    # adjacency matrix representation
    def primMST(self):

        #Key values used to pick minimum weight edge in cut
        key = [sys.maxint] * self.V
        parent = [None] * self.V # Array to store constructed MST
        key[0] = 0   # Make key 0 so that this vertex is picked as first vertex
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
            #print(parent)

        #print key
        #route = (self.getPath(parent))
        #return route

#PARAMETERS

#num_locs = 5
#g  = Graph(num_locs)
#total_time_max = 30
#personal_car = 'Yes'
#act_lvl = 0
#warning = True

#for each location, choose either car time or
#returns: (i.e. for 'A')[0 30 10 20 4]
data1 = [(u'232 East Ave, Ithaca, NY 14850, USA', u'111 Dryden Rd, Ithaca, NY 14850, USA', 120, 9.0, 849, 0.7)]
time = [(u'232 East Ave, Ithaca, NY 14850, USA', u'50'), (u'111 Dryden Rd, Ithaca, NY 14850, USA', u'50')]
own_vehicle = "no"
max_time = 4
activity_level = 50
'''
def construct_whole(data, time, own_vehicle, max_time, activity_level):
    g = Graph(len(time))
    matrix = []
    for i in range(len(time)): #for every row
        row = construct_row(data1, time, own_vehicle, max_time, activity_level) #populating a row
        matrix.append(row)
    g.graph = matrix
    g.primMST();
'''
def construct_whole(data1, time, own_vehicle, max_time, activity_level): #num_locs, personal_car, act_lvl
    #print time
    g = Graph(len(time))
    matrix = []
    accessories = []
    for i in range(len(time)):
        row = []
        acc = []
        #car_cost = []
        #using_uber = []
        for j in range(len(time)): #for every column
            est_loc_time = time[j][1]
            #print type(time)
            if (((own_vehicle == 'Yes') | (activity_level < 100)) | (est_loc_time > 5)): #loc_est_time
                t = data1[0][3] #Uber time
                a = ["Uber", est_loc_time, data1[0][5], data1[0][2]]
                #using_uber.append(data1[0][2])
            else:
                t = data1[0][4] #walking time
                if (j==i):
                    t = 0
                a = ["Walk", est_loc_time, data1[0][5], 0]

            row.append(t)
            acc.append(a)
            #car_cost.append(using_uber)
        matrix.append(row)
        accessories.append(acc)

    g.graph = matrix
    node_order = g.primMST()

    acc_time = accessories[node_order[0]][node_order[1]][1] + accessories[node_order[1]][node_order[2]][1]+accessories[node_order[2]][node_order[3]][1]+accessories[node_order[3]][node_order[4]][1]

    total_dist = accessories[node_order[0]][node_order[1]][2] +accessories[node_order[1]][node_order[2]][2] +accessories[node_order[2]][node_order[3]][2] +accessories[node_order[3]][node_order[4]][2]

    total_cost = accessories[node_order[0]][node_order[1]][3] +accessories[node_order[1]][node_order[2]][3] +accessories[node_order[2]][node_order[3]][3] +accessories[node_order[3]][node_order[4]][3]

    if acc_time > max_time:
        warning = "OVERTIME"
    else:
        warning = "NO WARNING"

    leg_info = '{"addresses": [' + time(node_order[0]) + '", "' + time(node_order[1]) + '", "'+ time(node_order[2]) + '", "'+ time(node_order[3]) + '", "' + time(node_order[4]) +'"],'
    leg1 = '"leg1": { "transport": ' + accessories[node_order[0]][node_order[1]][0] + ', "legTime": ' + accessories[node_order[0]][node_order[1]][1] + ', "legDist": ' + accessories[node_order[0]][node_order[1]][2] + ', "cost": ' + accessories[node_order[0]][node_order[1]][3]
    leg1 =  leg1 + '"},'
    leg2 = '"leg2": { "transport": ' + accessories[node_order[1]][node_order[2]][0] + ', "legTime": ' + accessories[node_order[1]][node_order[2]][1] + ', "legDist": ' + accessories[node_order[1]][node_order[2]][2] + ', "cost": ' + accessories[node_order[1]][node_order[2]][3]
    leg2 =  leg2 + '"},'
    leg3 = '"leg3": { "transport": ' + accessories[node_order[2]][node_order[3]][0] + ', "legTime": ' +  accessories[node_order[2]][node_order[3]][1] + ', "legDist": ' + accessories[node_order[2]][node_order[3]][2] + ', "cost": ' + accessories[node_order[2]][node_order[3]][3]
    leg3 =  leg3 + '"},'
    leg4 = '"leg4": { "transport": ' + accessories[node_order[3]][node_order[4]][0] + ', "legTime": ' +  accessories[node_order[3]][node_order[4]][1] + ', "legDist": ' + accessories[node_order[3]][node_order[4]][2] + ', "cost": ' + accessories[node_order[3]][node_order[4]][3]
    leg4 =  leg4 + '"},'
    ending =  '"totaltime" : ' + acc_time + ',"totaldistance": ' + totaldist + ',"totalcost": ' + totalcost + ',"warning": ' + warning
    ending = ending + '}"'

    finish =  leg_info + leg1 + leg2 + leg3 + leg4 + ending
    print finish

construct_whole(data1, time, own_vehicle, max_time, activity_level)
#g.graph = matrix
#g.primMST();

#if ( key > total_time_max):
#    warning = True

#str that was supposed to be a json file ....
# leg_info = """{"addresses": ['locA ', 'locB', 'locC', 'locD ', '+ locE + '],
#   "leg1": {
#     "transport": ' + transpA + ',
#     "legTime": ' + timeA + ',
#     "legDist": ' + distA + ',
#     "cost": ' + costA + '
#   },
#   "leg2": {
#     "transport": ' + transpB + ',
#     "legTime": ' + timeB + ',
#     "legDist": ' + distB + ',
#     "cost": ' + costB + '
#   },
#   "leg3": {
#     "transport": ' + transpC + ',
#     "legTime": ' + timeC + ',
#     "legDist": ' + distC + ',
#     "cost": ' + costC + '
#   },
#   "leg4": {
#     "transport": ' + transpD + ',
#     "legTime": ' + timeD + ',
#     "legDist": ' + distD + ',
#     "cost": ' + costD + '
#   },
#   "totaltime" : ' + acc_time + ',
#   "totaldistance": ' + totaldist + ',
#   "totalcost": ' + totalcost + ',
#   "warning": ' + warning + '
# }"""
#
# '''
# g = Graph(5)
# g.graph = [ [0, 2, 5, 6, 1],
#             [2, 0, 3, 8, 5],
#             [5, 3, 0, 2, 7],
#             [6, 8, 2, 0, 9],
#             [1, 5, 7, 9, 0],
#            ]
#
# result = g.primMST();
# result
# '''
