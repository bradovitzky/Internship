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
        for sink in start._sinks:
            if start._height > sink._height:
                print(start._name, "height:", start._height)
                print(sink._name, "height:", sink._height)
                print("connection capacity:", start._sinks[sink])
                if start._sinks[sink] >= start._height:
                    print(start._height, "packets transferred from", start._name, "to", sink._name)
                    print("The height of", sink._name, "is", sink._height, "and the height of", start._name, "is", start._height)
                    start._height = 0
                    sink._height += start._height
                    print("-------------------------------------------------------------------")
                elif start._sinks[sink] < start._height:
                    start._height -= start._sinks[sink]
                    sink._height += start._sinks[sink]
                    print(start._sinks[sink], "packets transferred to", sink._name, "from", start._name)
                    print("The height of", sink._name, "is", sink._height, "and the height of", start._name, "is", start._height)
                    print("-------------------------------------------------------------------")
                else:
                    print('Uh oh')
            elif:

        for s in start._sinks:
            print(s)
            self.sand_pile(s)
        return

#    def sand_pile(self):
#        '''What this code is trying to accomplish is to go through every node in a breadth first manner, checking
#        if the nodes that come after it have a smaller pile than themselves, and transferring their height if
#        necessary. A problem that I see arising here is that the checking and passing process should go in BACKWARDS
#        order so that it doesn't make a mistake with the heights, however that assumption may be wrong. Discuss this
#        code with dad ASAP.'''
#        listcycle = cycle(self._nodelist)
#        i = 0
#        while i <= self.numEdges:
#            i += 1
#            start = next(listcycle)
#            print("The current Start is", start)
#            nextnode = next(listcycle)
#            print("The current Nextnode is", nextnode)
#            if nextnode not in start._sinks:
#                start = next(listcycle)
#                print("The new nextnode is", nextnode)
#                print("The new start is", start)
#            while nextnode in start._sinks:
#                print("nextnode in start._sinks")
#                print(start._height, nextnode._height)
#                if start._height > nextnode._height:
#                    print(start._name, "height:", start._height)
#                    print(nextnode._name, "height:", nextnode._height)
#                    print("connection capacity:", start._sinks[nextnode])
#                    if start._sinks[nextnode] >= start._height:
#                        print(start._height, "packets transferred from", start._name, "to", nextnode._name)
#                        print("The height of", nextnode._name, "is", nextnode._height, "and the height of", start._name, "is", start._height)
#                        start._height = 0
#                        nextnode._height += start._height
#                        print("-------------------------------------------------------------------")
#                    elif start._sinks[nextnode] < start._height:
#                        start._height -= start._sinks[nextnode]
#                        nextnode._height += start._sinks[nextnode]
#                        print(start._sinks[nextnode], "packets transferred to", nextnode._name, "from", start._name)
#                        print("The height of", nextnode._name, "is", nextnode._height, "and the height of", start._name, "is", start._height)
#                        print("-------------------------------------------------------------------")
#                nextnode = next(listcycle)


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
    print("There are", g.numEdges, "edges in this graphs")
    g.traverse()
