class Graph():
    """The graph class instantiates a graph."""

    def __init__(self):
        self._table = {}

    def add_vertex(self, value):

        vertex = value
        self._table[vertex] = {}
        return vertex

    def add_edge(self, vertex_a, vertex_b, weight=None):
        

    def __repr__(self):
        # dictionary where the key is the value, and the value is a list of it's neighbors values.
        pass

    def __str__(self):
        pass


# class Vertex():
#     """The vertex class instantiates a node of a graph."""

#     def __init__(self, value):
#         self.value = {'value': value}

#     def __repr__(self):
#         pass

#     def __str__(self):
#         pass
