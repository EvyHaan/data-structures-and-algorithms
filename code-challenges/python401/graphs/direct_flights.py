from .graphs import Graph
from ..stacks_and_queues.stacks_and_queues import Queue


def final_destination(graph, lst):
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
                return 'False, 0'
        return 'True, {}'.format(total_cost)
