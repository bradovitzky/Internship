class Node(object):
    def __init__(self, name, height, ):
        self._name = name
        self._height = height
        self._sinks = []
        return

    def add_sink(self, node):
        self._sinks.append(node)
        return

    def print_all_neighbors(self):
        myString = "My name is: {}, I have: {} sinks: ".format(self._name, len(self._sinks))
        print(myString, ', '.join(str(p) for p in self._sinks))
        for sink in self._sinks:
            sink.print_all_neighbors()
        return

    def __str__(self):
        s = self._name
        return s


class Graph(object):
    def __init__(self):
        self._nodelist = []

    def add_node(self, node):
        self._nodelist.append(node)
        print('\n'.join(str(p) for p in self._nodelist))

if __name__ == "__main__":
    source = Node("source", 1)
    s = Node("s", 2)
    source.add_sink(s)
    o = Node("o", 3)
    source.add_sink(o)
    p = Node("p", 3)
    s.add_sink(p)
    q = Node("q", 3)
    o.add_sink(q)
    o.add_sink(p)
    sink = Node("sink", 0)
    p.add_sink(sink)
    q.add_sink(sink)
    print("no problem up to here")
    source.print_all_neighbors()

    g = Graph()
    g.add_node(source)
    g.add_node(s)
    g.add_node(o)
    g.add_node(p)
    g.add_node(q)

