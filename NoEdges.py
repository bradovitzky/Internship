class MyClass(object):
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, height, neighbors):
        self.nodes[name] = height, neighbors
        return