from random import randint

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

###########################################################
    def print_depth_first(self): #Note: unused
        myString = "My name is {} and I have {} sinks: ".format(self._name, len(self._sinks))
        print(myString, ', '.join(p._name for p in self._sinks))
        for sink in self._sinks:
            sink.print_all_neighbors()
        return
###########################################################

    def traverse_breadth_first(self):
        myString = "My name is {} and I have {} sinks: ".format(self._name, len(self._sinks))
        print(myString, ', '.join(p._name for p in self._sinks))
        self.print_sinks()
        return

    def print_sinks(self):
        for sink in self._sinks:
            myString = "I am {} and I have {} sinks: ".format(sink._name, len(sink._sinks))
            print(myString, ', '.join(p._name for p in sink._sinks))
        for s in self._sinks:
            s.print_sinks()
        return

    def __str__(self):
        name = self._name
        return name


class Graph(object):
    def __init__(self):
        self.numEdges = 0
        self._nodelist = []

    def add_node(self, node):
        self._nodelist.append(node)
        print('Node "', node, '" added to graph')

    def traverse(self):
        source = self._nodelist[0]
        self.sand_pile(source)
        return

    def sand_pile(self, start):
        for end in start._sinks:
            if len(start._sinks) == 1 or start == source:
                pass
            elif len(start._sinks) > 1:  # This section is executed if the selected node has multiple sinks
                randomizer = randint(1, len(start._sinks) - 1)
                end = list(start._sinks.keys())[randomizer]
            if start._height > end._height:
                print(start._name, "height:", start._height)
                print(end._name, "height:", end._height)
                print("connection capacity:", start._sinks[end])
                if start._sinks[end] >= start._height:
                    end._height += start._height
                    start._height -= start._height
                    print(start._height, "packets transferred from", start._name, "to", end._name)
                    print("The height of", end._name, "is", end._height, "and the height of", start._name, "is", start._height)
                elif start._sinks[end] < start._height:
                    start._height -= start._sinks[end]
                    end._height += start._sinks[end]
                    print(start._sinks[end], "packets transferred to", end._name, "from", start._name)
                    print("The height of", end._name, "is", end._height, "and the height of", start._name, "is", start._height)
            elif start._height == end._height:
                print(start._name, "height:", start._height)
                print(end._name, "height:", end._height)
                print("connection capacity:", start._sinks[end])
                print("The nodes have the same height. Going on to next node.")
            elif start._height < end._height:
                print(start._name, "height:", start._height)
                print(end._name, "height:", end._height)
                print("connection capacity:", start._sinks[end])
                print("The sink cannot receive more data. Going on to next node")
            if end == sink:
                end._height = 0
                print("Sink chewed up data")
            print("-------------------------------------------------------------------")
        for s in start._sinks:
            self.sand_pile(s)
        return

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
    source.traverse_breadth_first()

    g = Graph()
    g.add_node(source)
    g.add_node(s)
    g.add_node(o)
    g.add_node(p)
    g.add_node(q)
    for node in g._nodelist:
        for sinks in node._sinks:
            g.numEdges += 1
    print("There are", g.numEdges, "edges in this graph")
    g.traverse()
