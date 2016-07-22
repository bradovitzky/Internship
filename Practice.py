class Node(object):
    def __init__(self, n, h):
        self.n = n
        self.h = int(h)


class Edge(object):
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = int(c)


class CreateGraph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, name, height):
        node = Node(name, height)
        self.nodes[name] = height
        return

    def add_edge(self, source, sink, capacity):
        edge = Edge(source, sink, capacity)
        self.edges[edge] = capacity

    def make_it_flow(self, source, sink):
        for edge in self.edges: #For every edge in the graph
            if self.edges[source, sink] > sink.h: #if the source of the edge has more packets than the sink
                if self.edges[source, sink] >= source.h: #and if the capacity of the edge is greater than the height of the source
                    source.h = 0 #set the height of the source equal to 0
                    sink.h += source.h #and pass the packets over to the sink.
                elif self.edge[source, sink] < source.h: #If the capacity of the edge is smaller than the height of the source,
                    source.h -= self.edge[source, sink] #subtract the amount of packets that can go through from the source
                    sink.h += self.edge[source, sink] #and add them to the sink.

if __name__ == "__main__":
    g = CreateGraph()
    s = g.add_node("s", 4)
    o = g.add_node("o", 4)
    p = g.add_node("p", 4)
    q = g.add_node("q", 4)
    source = g.add_node("source", 1000)
    sink = g.add_node("sink", 0)
    g.add_edge(source, s, 2)
    g.add_edge(source, o, 2)
    g.add_edge(s, p, 2)
    g.add_edge(o, q, 2)
    g.add_edge(s, q, 1)
    g.add_edge(o, p, 1)
    g.add_edge(o, sink, 3)
    g.add_edge(q, sink, 3)
    g.make_it_flow(source, sink)
