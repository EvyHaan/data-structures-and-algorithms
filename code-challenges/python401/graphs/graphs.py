"""Graph Data Structure.

This module contains the Graph class with built-in methods.
"""
from ..stacks_and_queues.stacks_and_queues import Queue, Node


class Graph():
    """The graph class instantiates a graph."""

    def __init__(self):
        self._table = {}

    def add_vertex(self, value):
        """Adds a vertex to a graph.

        Args:
            value: the value of the vertex which becomes the key to reference the vertex object.
        """

        vertex = value
        self._table[vertex] = {}
        return vertex

    def add_edge(self, vertex_a, vertex_b, weight=None):
        """Adds an edge between two vertices in a graph.

        Args:
            vertex_a (dict): a reference to a vertex in a graph
            vertex_b (dict): a reference to a vertex in a graph
            weight (int): optional; the value assigned to the edge between vertices.
        """

        if vertex_a in self._table:
            if vertex_b in self._table and vertex_b not in vertex_a:
                self._table[vertex_a][vertex_b] = weight
                self._table[vertex_b][vertex_a] = weight

    def get_vertices(self):
        """Finds the vertices of a graph.

        Returns:
            vertices (list): a list of references to vertices in the graph.
        """

        vertices = []
        for key in self._table.keys():
            vertices.append(key)
        return vertices

    def get_neighbors(self, vertex):
        """Finds the neighbors of a vertex.

        Args:
            vertex (str): reference to a vertex to search the graph.

        Returns:
            neighbors (list): a list of tuples that references joined vertices and the weight of the connecting edge.
        """
        neighbors = []
        for key in self._table[vertex]:
            neighbors.append((key, self._table[vertex][key]))
        return neighbors

    def size(self):
        """Finds the size of a graph.

        Returns:
            size (int): a count of the vertices in the graph
        """
        size = 0
        for key in self._table.keys():
            size += 1
        return size

    def breadth_traversal(self, vertex):
        """Traverses a graph breadth-first.

        Args:
            vertex (str): reference to a vertex to search the graph.

        Returns:
            vertices (list): a list of vertices that are connected in some degree to the given vertex. Will not return island vertices.
        """
        que = Queue()
        visited = []
        vertices = []

        que.enqueue(vertex)
        visited.append(vertex)

        while que:
            current = que.dequeue()
            vertices.append(current)
            neighbors = self.get_neighbors(current)

            if len(neighbors) > 0:
                for neighbor in neighbors:
                    if neighbor[0] not in visited:
                        que.enqueue(neighbor[0])
                        visited.append(neighbor[0])
            else:
                return vertices
        return vertices

    def __repr__(self):
        temp_graph = self._table
        return '<Graph: {}>'.format(temp_graph)

    def __str__(self):
        temp_graph = self._table
        return 'This graph contains: {}'.format(temp_graph)
