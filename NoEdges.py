class Node():
    def __init__(self, name, height, ):
        self._name = name
        self._height = height
        self._sinks = []
        return

    def add_sink(self, node):
        self._sinks.append(node)
        return

    def print_all_sinks(self):
        myString = "My name is: {}, I have: {} sinks".format(self._name, len(self._sinks))
        print(myString)
        for sink in self._sinks:
            sink.print_all_sinks()
        return

    def __str__(self):
        s = self._name
        return s


if __name__ == "__main__":
    print("Hello")
    n = Node("start", 1)
    print(n)
    m = Node("next_up", 2)
    print(m)
    n.add_sink(m)
    m = Node("next_down", 3)
    print(m)
    n.add_sink(m)
    m = Node("next_", 2)
    print(m)
    n.add_sink(m)
    print("no problem up to here")

    n.print_all_sinks()