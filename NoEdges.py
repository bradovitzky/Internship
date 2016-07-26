from itertools import cycle

class Node(object):
    def __init__(self, name, height):
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
        self.numEdges = 0
        self._nodelist = []
        self._path = []

    def add_node(self, node):
        self._nodelist.append(node)
        print('Node "', node, '" added to graph')

    def sand_pile(self):
        listcycle = cycle(self._nodelist)
        i = 0
        while i <= self.numEdges:
            i += 1
            start = next(listcycle)
            nextnode = next(listcycle)
            if nextnode not in start._sinks:
                start = next(listcycle)
            while nextnode in start._sinks:
                if start._height > nextnode._height:
                    print(start._name, "height:", start._height)
                    print(nextnode._name, "height:", nextnode._height)
                    print("connection capacity:", start._sinks[nextnode])
                    if start._sinks[nextnode] >= start._height:
                        print(start._height, "packets transferred from", start._name, "to", nextnode._name)
                        print("The height of", nextnode._name, "is", nextnode._height, "and the height of", start._name, "is", start._height)
                        start._height = 0
                        nextnode._height += start._height
                        print("-------------------------------------------------------------------")
                    elif start._sinks[nextnode] < start._height:
                        start._height -= start._sinks[nextnode]
                        nextnode._height += start._sinks[nextnode]
                        print(start._sinks[nextnode], "packets transferred to", nextnode._name, "from", start._name)
                        print("The height of", nextnode._name, "is", nextnode._height, "and the height of", start._name, "is", start._height)
                        print("-------------------------------------------------------------------")
                nextnode = next(listcycle)


if __name__ == "__main__":
    source = Node("source", 10000)
    s = Node("s", 0)
    source.add_sink(s, 10)
    o = Node("o", 0)
    source.add_sink(o, 10)
    p = Node("p", 0)
    s.add_sink(p, 10)
    q = Node("q", 0)
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
    for node in g._nodelist:
        for sinks in node._sinks:
            g.numEdges += 1
    print("There are", g.numEdges, "edges in this graphs")
    g.sand_pile()
