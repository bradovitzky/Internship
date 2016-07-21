class Node(object):
    def __init__(self, n, h):
        self.name = str(n)
        self.height = int(h)

class Edge(object):
    def __init__(self, u, v, c):
        self.source = u
        self.sink = v
        self.capacity = c

class SandPiler(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.flow = {}

    def add_node(self, n, h):
        node = Node(n, h)
        self.nodes.append(node)

    def add_edge(self, u, v, w):
        if u == v:
            raise ValueError("The source is the same point as the sink")
        else:
            edge = Edge(u, v, w)
            self.edges[u].append(edge)
            self.flow[edge] = 0
        print("Edges: " + self.edges + ", Flow: " + self.flow)

    def get_edges(self, v):
        return self.edges[v]

    def sand_pile(self, source, sink):
        source = Node(source)
        sink = Node(sink)
        if source == sink:
            stop
#The following code is where the sand-piling algorithm is actually implemented.
        for edge in self.get_edges(source):
            if edge.source > edge.sink:
                if edge.capacity >= source.height:
                    source.height = 0
                    sink.height += source.height
                    print(source.height, " packets transferred from " + edge.source, "to " + edge.sink)
                elif edge.capacity < source.height:
                    source.height -= edge.capacity
                    sink.height += edge.capacity


if __name__ == "__main__":
    g = SandPiler()
    for l in "sopq":
        g.add_node(l, 4)
    g.add_node("source", 1000)
    g.add_node("sink", 0)
    g.add_edge("source", "s", 2)
    g.add_edge("source", "o", 2)
    g.add_edge("s", "p", 2)
    g.add_edge("o", "q", 2)
    g.add_edge("s", "q", 1)
    g.add_edge("o", "p", 1)
    g.add_edge("o", "sink", 3)
    g.add_edge("q", "sink", 3)
    g.get_edges("sink")
    g.sand_pile("source", "sink")


