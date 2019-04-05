from .graphs import Graph, Vertex


def test_vertex_exists():
    assert Vertex


def test_vertex_instance():
    value = 4
    assert Vertex(value)


def test_graph_exists():
    assert Graph


def test_graph_instance():
    assert Graph()


def test_add_one_vertex():
    g = Graph()
    vertex = g.add_vertex('apple')
    assert vertex
    assert vertex.value is 'apple'
    assert 'apple' in g._table


def test_add_two_vertex():
    g = Graph
    vertex = g.add_vertex('apple')
    vertex = g.add_vertex('banana')
    assert 'apple' in g._table
    assert 'banana' in g._table


def test_one_edge():
    g = Graph
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    g.add_edge(apple, banana, 4)

    assert g._table['apple'] == '???'
    assert g._table['banana'] == '???'


def test_get_vertices():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    g.get_vertices()

    assert vertices == '???'


def test_get_neightbors():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    g.get_neighbors()

    assert neighbors == '???'


def test_graph_size():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    assert len(g) == 2
