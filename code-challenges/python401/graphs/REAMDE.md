# Graphs

## Challenge
Implement a Graph.
<br />
<br />
The structure of the implemented graph is a dictionary whose keys are a reference to its vertices, and it's values are the vertices themselves. The keys are named by the value they contain. Each vertex is also a dictionary. Here, the keys are a reference to a neighbor node, and the value is the weight of the edge that connects them.
<br />
<br />
```Graph = { Vertex: { Neighbor: Weight } }```


## API
- **.add_vertex()**
    - adds a new vertex with a value to a Graph.
    - *Efficiency*: Space: O(1) Time: O(1)
- **.add_edge()**
    - adds a reference to a new edge between two vertices in a Graph.
    - *Efficiency*: Space: O(1) Time: O(1)
- **.get_vertices()**
    - finds all vertices in a Graph.
    - *Efficiency*: Space: O(n) Time: O(n)
- **.get_neighbors()**
    - finds all neighbors connected to a given vertex, as well as the weight of the connecting edge.
    - *Efficiency*: Space: O(n) Time: O(n)
- **.size()**
    - finds the size of the Graph by counting the vertices within it.
    - *Efficiency*: Space: O(1) Time: O(n)
- **.breadth_traversal()**
    - conducts a breadth-first traversal of a Graph.
    - *Efficiency*: Space: O(n) Time: O(n)

## Method Solutions
![graph_breadth_traversal](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/graph_breadth_traversal/assets/graph_breadth_traversal.jpg)

## Additional Challenges

### Direct Flights Challenge
Given a graph of connected cities and a list of cities, determine if the trip can be made through direct flights or not. Return 'True' and the cost if it can, or 'False' and '$0' if it can't.

![direct_flights](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/direct_flights/assets/direct_flights.jpg)