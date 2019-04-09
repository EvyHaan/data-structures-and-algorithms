from .graphs import Graph


def test_graph_exists():
    assert Graph


def test_graph_instance():
    assert Graph()


def test_add_one_vertex():
    g = Graph()
    vertex = g.add_vertex('apple')
    assert vertex
    assert 'apple' in g._table


def test_add_two_vertex():
    g = Graph()
    appple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    assert 'apple' in g._table.keys()
    assert 'banana' in g._table.keys()


def test_one_edge():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    g.add_edge(apple, banana, 4)

    assert g._table['apple']['banana'] == 4
    assert g._table['banana']['apple'] == 4


def test_two_edges():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    fig = g.add_vertex('fig')
    g.add_edge(apple, banana, 4)
    g.add_edge(apple, fig, 5)

    assert g._table['apple']['banana'] == 4
    assert g._table['banana']['apple'] == 4
    assert g._table['apple']['fig'] == 5
    assert g._table['fig']['apple'] == 5


def test_get_vertices_empty_graph():
    g = Graph()
    assert g.get_vertices() == []


def test_get_vertices_two():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    assert g.get_vertices() == ['apple', 'banana']


def test_get_4_vertices():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    fig = g.add_vertex('fig')
    plum = g.add_vertex('plum')

    assert g.get_vertices() == ['apple', 'banana', 'fig', 'plum']


def test_get_three_neighbors():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    fig = g.add_vertex('fig')
    plum = g.add_vertex('plum')
    g.add_edge(apple, banana, 4)
    g.add_edge(apple, fig, 5)
    g.add_edge(apple, plum, 5)

    g.get_neighbors('apple')

    assert g.get_neighbors('apple') == [('banana', 4), ('fig', 5), ('plum', 5)]


def test_graph_size():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    assert g.size() == 2


def test_btraversal_one_vertex():
    g = Graph()
    apple = g.add_vertex('apple')
    assert g.breadth_traversal('apple') == ['apple']


def test_btraversal_two_vertex():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    g.add_edge(apple, banana, 4)
    # import pdb; pdb.set_trace()

    assert g.breadth_traversal('apple') == ['apple', 'banana']


def test_traversal_multiple_neighbors():
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    fig = g.add_vertex('fig')
    plum = g.add_vertex('plum')
    g.add_edge(apple, banana, 4)
    g.add_edge(apple, fig, 5)
    g.add_edge(apple, plum, 5)

    assert g.breadth_traversal('apple') == ['apple', 'fig', 'banana', 'plum']


def test_btraversal_shared_neighbor():
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    fig = g.add_vertex('fig')
    plum = g.add_vertex('plum')
    g.add_edge(apple, banana, 4)
    g.add_edge(apple, fig, 5)
    g.add_edge(apple, plum, 5)
    g.add_edge(plum, banana, 4)

    assert g.breadth_traversal('apple') == ['apple', 'fig', 'banana', 'plum']


def test_btraversal_island():
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    fig = g.add_vertex('fig')
    plum = g.add_vertex('plum')
    g.add_edge(apple, banana, 4)
    g.add_edge(apple, plum, 5)
    g.add_edge(plum, banana, 4)

    assert g.breadth_traversal('apple') == ['apple', 'banana', 'plum']
