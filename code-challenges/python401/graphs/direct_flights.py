from .graphs import Graph
from ..stacks_and_queues.stacks_and_queues import Queue


def final_destination(graph, lst):
    """Determines if all stops in an itenerary are possible through direct flights.

    Args:
        graph: a graph of locations to be searched.
        lst (lst): a list of cities in an itinerary.

    Returns:
        'True, <cost>' (str): If the cities are connected by successive direct flights, a string returns 'True' and the total cost of connecting flights.
        'False, 0' (str): If the cities are not connected by successive direct flights, a string returns 'False' and implies a cost of $0.
    """
    total_cost = 0
    itinerary = Queue()

    for city in lst:
        itinerary.enqueue(city)

    while itinerary.front:
        current = itinerary.dequeue()
        neighbors = graph.get_neighbors(current)
        for neighbor in neighbors:
            if neighbor[0] == itinerary.front:
                total_cost += neighbor[i]
                break
            else:
                return 'False, $0'
        return 'True, ${}'.format(total_cost)
