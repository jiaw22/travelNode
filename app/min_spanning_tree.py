# # Reference: Geeks for Geeks
# # A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# # The program is for adjacency matrix representation of the graph
#
# import sys  # Library for INT_MAX
#
# class Graph():
#
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                       for row in range(vertices)]
#
#     # A utility function to print the constructed MST stored in parent[]
#     def printMST(self, parent):
#         print "Edge \tWeight"
#         for i in range(1,self.V):
#             print parent[i],"-",i,"\t",self.graph[i][ parent[i] ]
#
#     # A utility function to find the vertex with minimum distance value, from
#     # the set of vertices not yet included in shortest path tree
#     def minKey(self, key, mstSet):
#
#         # Initilaize min value
#         min = sys.maxint
#
#         for v in range(self.V):
#             if key[v] < min and mstSet[v] == False:
#                 min = key[v]
#                 min_index = v
#
#         return min_index
#
#     # Function to construct and print MST for a graph represented using
#     # adjacency matrix representation
#     def primMST(self):
#
#         #Key values used to pick minimum weight edge in cut
#         key = [sys.maxint] * self.V
#         parent = [None] * self.V # Array to store constructed MST
#         key[0] = 0   # Make key 0 so that this vertex is picked as first vertex
#         mstSet = [False] * self.V
#
#         parent[0] = -1  # First node is always the root of
#
#         for cout in range(self.V):
#
#             # Pick the minimum distance vertex from the set of vertices not
#             # yet processed. u is always equal to src in first iteration
#             u = self.minKey(key, mstSet)
#
#             # Put the minimum distance vertex in the shortest path tree
#             mstSet[u] = True
#
#             # Update dist value of the adjacent vertices of the picked vertex
#             # only if the current distance is greater than new distance and
#             # the vertex in not in the shotest path tree
#             for v in range(self.V):
#                 # graph[u][v] is non zero only for adjacent vertices of m
#                 # mstSet[v] is false for vertices not yet included in MST
#                 # Update the key only if graph[u][v] is smaller than key[v]
#                 if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
#                         key[v] = self.graph[u][v]
#                         parent[v] = u
#             #print(parent)
#
#         #print key
#         self.printMST(parent)
#
# #PARAMETERS
#
# num_locs = 5
# g  = Graph(num_locs)
# total_time_max = 30
# personal_car = 'Yes'
# act_lvl = 0
# warning = True
#
# #for each location, choose either car time or
# #returns: (i.e. for 'A')[0 30 10 20 4]
# def narrow_down(num_locs, personal_car, act_lvl):
#     for k in range(num_locs):
#         current_leg = #API shit
#         if (personal_car == 'Yes') || (act_lvl < 100) || (leg_est_time > 5): #global user
#             time = car_time #API
#         else:
#             time = walk_time #API
#
#
# #constructing matrix
# matrix = []
# for i in range(num_locs):
#     row = []
#     for j in range(num_locs):
#         row.append(...)
#     matrix.append(row)
#
# g.graph = matrix
# g.primMST();
#
# if ( key > total_time_max):
#     warning = True
#
# #str that was supposed to be a json file ....
# leg_info = """{"addresses": ['+ locA + ', '+ locB +', '+ locC +', '+ locD + ', '+ locE + '],
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
