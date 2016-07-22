class Node(object):
    def __init__(self, name, height, ):
        self._name = name
        self._height = height
        self._sinks = {}
        return

    def add_sink(self, node, capacity):
        self._sinks[node] = capacity
        print("Connection created between", self._name, "and", node, "with capacity", capacity)
        return

    def print_all_neighbors(self):
        myString = "My name is {} and I have {} sinks: ".format(self._name, len(self._sinks))
        print(myString, ', '.join(str(p) for p in self._sinks))
        for sink in self._sinks:
            sink.print_all_neighbors()
        return

    def __str__(self):
        name = self._name
        return name


class Graph(object):
    def __init__(self):
        self._nodelist = []

    def add_node(self, node):
        self._nodelist.append(node)
        print('Node "', node, '" added to graph')

if __name__ == "__main__":
    source = Node("source", 1)
    s = Node("s", 2)
    source.add_sink(s, 10)
    o = Node("o", 3)
    source.add_sink(o, 10)
    p = Node("p", 3)
    s.add_sink(p, 10)
    q = Node("q", 3)
    o.add_sink(q, 10)
    o.add_sink(p, 10)
    sink = Node("sink", 0)
    p.add_sink(sink, 10)
    q.add_sink(sink, 10)
    source.print_all_neighbors()

    g = Graph()
    g.add_node(source)
    g.add_node(s)
    g.add_node(o)
    g.add_node(p)
    g.add_node(q)

