class Graph():
    """"""

    def __init__(self):
        self._table = {}

    def add_vertex(self, value):

        vertex = Vertex(value)

        self._table[value] = []
        return Vertex

    def add_edge(self, weight=None):
        pass

    def __repr__(self):
        # dictionary where the key is the value, and the value is a list of it's neighbors values.
        pass

    def __str__(self):
        pass


class Vertex():
    """The vertex class instantiates a node of a graph."""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        pass

    def __str__(self):
        pass
