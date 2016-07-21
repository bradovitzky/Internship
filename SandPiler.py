class Node(object):
    def __init__(self, h, n):
        self.height = int(h)
        self.name = n

    def __repr__(self):
        return 'Height=%s' % self.height


class Edge(Node):
    def __init__(self, u, v, w):
        self.source = Node.__init__(self, int(), u)
        self.sink = Node.__init__(self, int(), v)
        self.capacity = int(w)

    def __repr__(self):
        return 'Source=%s -> Sink=%s: Capacity=%s' % (self.source, self.sink, self.capacity)


class Network(object):
    def __init__(self):
        self.nodeDict = {}
        self.adj = {}
        self.flow = {}

    def add_node(self, node):
        self.adj[node] = []
        self.nodeDict[node] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        else:
            edge = Edge(u, v, w)
            self.adj[u].append(edge)
            self.flow[edge] = 0
        print(self.adj, self.flow)

    def sand_pile(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            if edge.source > edge.sink:
                if edge.capacity >= source.height:
                    source.height = 0
                    sink.height += source.height
                elif edge.capacity < source.height:
                    source.height -= edge.capacity
                    sink.height += edge.capacity

if __name__ == "__main__":
    g = Network()
    [g.add_node(v) for v in "sopqrt"]
    g.add_edge('s', 'o', 3)
