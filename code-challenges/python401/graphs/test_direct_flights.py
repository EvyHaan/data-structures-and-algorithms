from .direct_flights import final_destination
from .graphs import Graph


def test_two_cities():
    g = Graph()
    seattle = g.add_vertex('seattle')
    portland = g.add_vertex('portland')
    maui = g.add_vertex('maui')
    rochester = g.add_vertex('rochester')
    nola = g.add_vertex('nola')
    sanfran = g.add_vertex('sanfran')
    nyc = g.add_vertex('nyc')
    atlantis = g.add_vertex('atlantis')

    g.add_edge(seattle, portland, 200)
    g.add_edge(seattle, rochester, 400)
    g.add_edge(portland, maui, 300)
    g.add_edge(portland, sanfran, 200)
    g.add_edge(nola, sanfran, 200)
    g.add_edge(nola, nyc, 300)
    g.add_edge(nyc, rochester, 100)
    g.add_edge(nola, rochester, 300)

    lst = ['seattle', 'rochester']

    assert final_destination(g, lst) == 'True, 400'
