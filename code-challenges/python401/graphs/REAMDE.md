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