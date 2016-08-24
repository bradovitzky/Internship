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
        self._height = int(height)
        self._sinks = {}
        return

    def getName(self):
        return self._name

    def add_sink(self, node, capacity):
        self._sinks[node] = int(capacity)
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
        self._nodes = {}
        self._levels = {}
        self._maxDepth = int()
        self._treeList = []
        return

    def add_node(self, node):
        name = node.getName()
        self._nodes[name] = node
        print('Node "', node, '" added to graph with height', node._height)
        return

    def getNodeByName(self, name):
        return self._nodes[name]

    def traverse(self):
        source = self._nodes[0]
        print(source._name, source._height)
        self.sand_pile(source)
        return

    def readFromFile(self, fileName):
        f = open(fileName, 'r')
        lines = f.readlines()
        # first pass to create all the nodes without edges
        for line in lines:
            lineList = line.split()
            print(lineList)
            if line[0] == '#': # skip comment lines
                continue
            newNode = Node(lineList[0], lineList[2])
            depth = lineList[1] # currently useless
            if depth not in self._levels:
                self._levels[depth] = [newNode]
            else:
                self._levels[depth].append(newNode) # will eventually remove levels and depth
            self.add_node(newNode)
            print("New node created with name", lineList[0], "and height", lineList[2], "on level", lineList[1])

        # second pass to create edges
        n = 0
        for line in lines:
            lineList = line.split()
            # pull all the nodes of the graph already created
            myName = lineList[0]
            if myName == '#': # skip comment lines
                continue
            myNode = self.getNodeByName(myName)
            # retrieve list of sink names from file
            sinkNames = []
            sinkCapacities = []
            if len(lineList) == 3:
                print("This is the final node and has no sinks")
            for element in lineList[3:]: # change to [2:] after levels and depth get removed
                if not is_number(element):
                    print(element, "added to 'sinks'")
                    sinkNames.append(element)
                else:
                    print(element, "added to 'capacities'")
                    sinkCapacities.append(element)


            # link sinks to myNode
            i=0
            for sinkName in sinkNames:
                sink = self.getNodeByName(sinkName)
                myNode.add_sink(sink, sinkCapacities[i])
                i += 1

            n += 1
        return

    def breadthFirstTraverse(self):
        self._maxDepth = max(self._levels)
        for lvl in sorted(self._levels.keys()):
            lvlList = []
            lvlList.append(self._levels.get(lvl))
            self._treeList += lvlList
            for list in lvlList:
                for node in list:
                    self.sand_pile(node)
        return

    def sand_pile(self, start):
        for end in start._sinks:
            if len(start._sinks) > 1:  # This section is executed if the selected node has multiple sinks
                randomizer = randint(1, len(start._sinks) - 1)
                end = list(start._sinks.keys())[randomizer]
            if start._height > end._height: # try to send some data
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
    g.readFromFile("Graph.txt")
    g.breadthFirstTraverse()
