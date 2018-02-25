''' citing '''
from collections import defaultdict
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    #self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = defaultdict(list) #{}
  nodes = set(graph.nodes)

  while nodes:          #frontier/nodes is not empty
    min_node = None
    for node in nodes:
      print "visited: ", visited
      if node in visited:
          print "1"
          if min_node is None:
              print "2"
              min_node = node    #simply add node to start somewhere
          elif visited[node] < visited[min_node]:
              print "3"
              min_node = node

    if min_node is None:
      break

    nodes.remove(min_node) #remove f from F
    current_weight = visited[min_node]
    print "current_weight: ", current_weight
    print "min node: ", min_node

    for edge in graph.edges[min_node]: #for each edge(f,w)
      if edge not in visited:
          weight = current_weight + graph.distances[(min_node, edge)] #L[f] + wgt(f,w)
          path[edge].append((min_node))
          visited.update({min_node:weight})
      else:
        if current_weight + graph.distances[(min_node, edge)] < visited[edge]:
            visited[edge] = current_weight


  return visited, path #visdited,path

g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')

g.add_edge('A','B',12)
g.add_edge('A','C',7)
g.add_edge('B','D',1)
g.add_edge('B','A',12)
g.add_edge('D','E',8)
g.add_edge('C','F',3)
g.add_edge('D','G',5)
g.add_edge('F','B',3)
g.add_edge('F','G',2)
g.add_edge('C','D',13)
g.add_edge('E','B',6)

'''
g = Graph()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')

g.add_edge('a','b',1)
g.add_edge('b','a',1)
g.add_edge('b','c',4)
g.add_edge('c','b',4)
g.add_edge('a','c',2)
g.add_edge('c','a',2)
g.add_edge('c','d',3)
g.add_edge('d','c',3)
'''
print(dijsktra(g,'A'))
