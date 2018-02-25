from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp
#jsonify function pass that into a variable, variable.field
# get from

#INPUTS
#values gotten from other APIs:
#for each given edge:
# -> transp_pref: (input parameter from user)
# -> A-B_car_time: (from Google/Lyft API)
# -> A-B_edge_cost: (from Lyft API)
# -> A-B_walk_time: (from Google API)
#
def create_graph(locs, graph):
    for i in range(len(locs)):
        list_rest = []
        to_append = locs[i] #node to append to assoc list
        del locs[i]

        #add the rest of the list as the connected nodes
        for (j = 0; j < len(locs); j++):
            list_rest.append({locs[j]:(car_time, walk_time)}) #API
        graph.update(to_append,list_rest)
        locs.append(to_append) #add again for next iteration of assoc list

def narrow_down_times(locs, graph, personal_car, act_lvl):
    new_graph = {}
    for (i = 0; i < len(locs); i++): #iterate
        #to_examine = locs[i]
        list_rest = []
        for (j = 0; j < len(graph.get(i)); j++):
            #basic constraints on what the algorithm chooses to do with user
            #preferences
            if (personal_car == 1) || (act_lvl < 100):
                time = car_time
            else:
                time = walk_time
            list_rest.append((locs[j],time))

        new_graph.update({locs[i],list_rest})

#dijkstra: graph=[{'A',30}...], start='A',end='E',
def dijkstra(graph, start, end, path=[],acc_time):
    path = path + [start]
    acc_time = 0
    while (graph != {}):
        list_vals = []
        list_keys = []
        #f = node in F with min L value
        for (i = 0; i < len(graph.get(start)); i++):
            list_vals.append((graph.get(start)[i])[1])
            list_keys.append((graph.get(start)[i])[0])
        v = min(list_vals) #going to a node of min time
        k =  list_keys[list_vals.index(v)] #key of min time
        for node in graph.get(start):
            if node[0] not in path:
                acc_time = acc_time + node[1]
                path = path + [node]
            else:
                node_srch_list = graph.get(node[0])
                if (acc_time + node[1] < node_srch_list[start]): #acc_time
                    acc_time = acc_time + node[1]

    '''
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
         if node not in path: #if node in the frontier set
             newpath = find_shortest_path(graph, node, end, path)
             if (acc_time +  < len(shortest)):
                shortest = newpath
    return shortest
    '''

if (acc_time_at_places > total_max_time):
    print("reassess expected time as input")

    #solver = pywrapcp.Solver("travel_node_scheduling")


#for each given node:
# -> avg_time_at_given_loc: (input parameter from user)
# ->
#generate solutions!

#cumulative sum of time spent (either via car / walk) = acc_time

#Constraints:
# acc_time cannot exceed max_time (from user)

def main():
  # definite user inputs:
  total_max_time = #user input
  acc_time_at_places = #sum total of avg time of all locs
  graph = {}
  create_graph(locs, graph)
  opt_graph = narrow_down_times(locs, graph, personal_car, act_lvl)







  num_locs = 4 #number
  personal_car = 0 # 1 if there is a car
  activity_lvl = 0 #0,1,2
  total_time_max = -1 #integer; -1 if not provided (any amount of time)
  node_options = {'Loc': trvl_to_node ,'Car Time': 20, 'Walk Time': 40}

  # Creates the solver.
  solver = pywrapcp.Solver("travel_node_scheduling")

  #determine car vs. walk FOR EACH EDGE

  solver.Add(calcTime <= reccTime);
# Creates the variables.
  recTime1 = #given by program
  recTime2 = #given by program
  recTime3 = #given by program
  #
  total_edges = num_locs - 1

  edge1_time = solver.IntVar(0, recTime1, "e1") #we're just putting recommended time
  edge2_time = solver.IntVar(0, recTime2, "locB")
  edge3_time = solver.IntVar(0, recTime3, "locC")


  solver.Add(edge_time <= total_time_max) #adding constraint
  solver.Add(personal_car == False) #if true, gives more freedom
  solver.Add(activity_lvl != 0) #if 1, 2 instead, gives more freedom

  #more global solver constraint (for 2nd solver)
  solver.Add(total_time_max != -1)

  db = solver.Phase([x, y, z], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
  solver.Solve(db)






  '''
  solver = pywrapcp.Solver("travel_node_scheduling")
  num_vals = 3
  x = solver.IntVar(0, num_vals - 1, "x") # transportation preference
  y = solver.IntVar(0, num_vals - 1, "y")
  z = solver.IntVar(0, num_vals - 1, "z")

  # Create the constraints.

  solver.Add(x!=y) # time limit
# Create the decision builder.
  db = solver.Phase([x, y, z], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
  solver.Solve(db)
  count = 0

  while solver.NextSolution():
    count += 1
    print("Solution", count, '\n')
    print("x = ", x.Value())
    print("y = ", y.Value())
    print("z = ", z.Value())
    print()
  print("Number of solutions:", count)
'''
if __name__ == "__main__":
  main()
