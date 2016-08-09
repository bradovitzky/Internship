from random import randint


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


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
        self._nodelist = []
        self._levels = {}
        self._maxDepth = int()
        self._treeList = []

    def add_node(self, node):
        self._nodelist.append(node)
        print('Node "', node, '" added to graph with height', node._height)

    def traverse(self):
        source = self._nodelist[0]
        print(source._name, source._height)
        self.sand_pile(source)
        return

    def breadthFirstTraverse(self):
        f = open("Graph.txt", 'r')
        for line in f.readlines():
            lineList = line.split()
            print(lineList)
            if "NODE" in line:
                continue
            newNode = Node(lineList[0], lineList[2])
            depth = lineList[1]
            self._levels[depth] = newNode
            self.add_node(newNode)
            print("New node created with name", lineList[0], "and height", lineList[2], "on level", lineList[1]);
            if len(lineList) == 3:
                print("This is the final node and has no sinks")
            else:
                lineList.pop(0)
                lineList.pop(0)
                lineList.pop(0)
                print(lineList)
                sinks = []
                values = []
                for element in lineList:
                    if not is_number(element):
                        print(element, "added to 'sinks'")
                        sinks.append(element)
                    elif is_number(element):
                        print(element, "added to 'values'")
                        values.append(element)
                for i in range(len(sinks)):
                    print(sinks[i])
                    print(values[i])
                    sink = Node(sinks[i], int())
                    newNode.add_sink(sink, values[i])
                    # newNode.traverse_breadth_first()
        self._maxDepth = max(self._levels)
        for lvl in sorted(self._levels.keys()):
            lvlList = []
            lvlList.append(self._levels.get(lvl))
            self._treeList += lvlList
            for node in lvlList:
                self.sand_pile(node)

    def sand_pile(self, start):
        for end in start._sinks:
            if len(start._sinks) > 1:  # This section is executed if the selected node has multiple sinks
                randomizer = randint(1, len(start._sinks) - 1)
                end = list(start._sinks.keys())[randomizer]
            if start._height > start._height:
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
            if len(end._sinks) == 0:
                end._height = 0
                print("Sink height reset to", end._height)
            print("-------------------------------------------------------------------")
        return

if __name__ == "__main__":

    g = Graph()
    g.breadthFirstTraverse()
