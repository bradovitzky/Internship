"""This program has the following purpose:
 Given a flow network with vertices, edges, capacities, and an initial
 flow value, it will iterate, increasing the flow value by 1 unit each
 time. At each iteration, it will find the augmenting path along the 
 residual network, and augment the flow along that path. This is, in
 essence, an implementation of the Ford-Fulkerson algorithm of max-flow
 min-cut."""

#First I will create a type: the Edge. It will be composed of a source,
# a sink, and a capacity.

class Edge(object):
	#initializing variables u, v, and c for the aforementioned elements
 	def __init__(self, u, v, c):
 		self.source = u
 		self.sink = v
 		self.capacity = c

#Next, I will create an object type that will generate a flow network
# based on the user's input of vertices, edges, and capacities. Then,
# it will take this data and find the residual network, and the
# augmentation path to follow and augment. Once it can't find any more
# paths to follow, it will terminate and return the maximum flow.

 class FlowNetwork(object):
 	def __init__(self):
 		
 	def add_vertex():
 		
 	def add_edge():
