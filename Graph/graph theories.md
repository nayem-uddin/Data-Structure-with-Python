## **Basics of Graph**

- A graph is a non-linear data structure consisting of nodes/vertices and edges.
- The mathematical expression of a graph is G = (V,E)  
   G=graph  
   V=No. of vertices  
   E=No. of edges
- A graph in which the directions of the edges are mentioned is called a `directed graph`. Otherwise, the graph is called an `undirected graph`.
- Directions of the edges of a directed graph are unidirectional, and those of the edges of an undirected graph are bi-directional.
- The edges of an undirected graph have no direction indication. Hence, they are considered bi-directional.
- A `weighted graph` is a graph with value-assigned edges. The opposite is called `unweighted`.
- A graph having cycle(s) is a `cyclic graph`. The opposite is `acyclic`. (Cyclic means a path starting from a node ends at the same node.)
- Tree is an example of an acyclic graph.
- A graph with no. of edges close to the maximum is called a `dense graph`. The opposite is called a `sparse graph`.
- Terms related to graph:
  - **Adjacent/Neighbor nodes:** Two nodes connected through a single edge.
  - **Path:** Sequence of nodes, each pair connected through an edge.
  - **Length of a path:** The length of a path refers to the no. of edges.
  - **Simple path:** A path with no repeating node.
  - **Closed path:** A path having the same node as its starting and ending node.
  - **Cycle:** A path starting from and ending at the same node, the other nodes being distinct.
  - **Connected graph:** A graph having a path to reach a node from any other node. The opposite is called a `disconnected graph`.
  - **Strongly connected graph:** A directed graph having a directed path to reach a node from any other node. The opposite is called a `weakly connected graph`.
  - **Degree of a node:** The no. of edges connected to a node in an undirected graph.
  - **Indegree of a node:** The no. of edges ending at a node in a directed graph.
  - **Outdegree of a node:** The no. of edges starting from a node in a directed graph.
  - **Complete graph:** A graph having an edge between each pair of nodes.
  - **Adjacency matrix:**
    - Matrix representation of the connections between the nodes.
    - It is a k\*k matrix, where k is the no. of nodes.
    - For an unweighted graph, it is a matrix with 1s and 0s, where 1 indicates an edge between the nodes, and 0 represents the opposite.
    - For a weighted graph, the 1s are replaced with the weights of the edges.
  - Adjacency list:
    - Represented with key-value pairs, where each key is a node and its value is the list of the nodes connected to it, or the list of some pairs, where each pair consists of the connected node and the weight of the edge.

### Graph with Multiple Edges

- In the adjacency matrix representation of an unweighted undirected graph, the values represents the no. of edges connecting the nodes.
- In the adjacency list representation of an unweighted undirected graph, there may be multiple instances of a node in the nodes' list of any node.

## **Graph Traversal Algorithms**

- **DFS**
  - Depth First Search
  - Traversal starts from the starting node. Choosing the starting node is arbitrary.
  - Visits the unvisited adjacent node to each node. If there are multiple unvisited adjacent nodes to a node, anyone can be chosen first.
  - This process continues until we reach the dead-end visiting all the nodes.
  - If a node has multiple adjacent nodes in such a way that visiting one node fron another adjacent node is impossible except through their parent node (the node both of them connected with), then visiting the unvisited node becomes possible with backtracking (backtracking means returning to the parent node).
  - DFS implementation with stack:
    - Push a node to the stack and pop that.
    - Check if that node is unvisited
    - If that node is unvisited, then visit that node and push its adjacent nodes to the stack.
    - Repeat the process for each of the nodes until all the nodes are visited.
- **BFS**
  - Breadth First Search
  - A level-order traversal algorithm
  - Starts at an arbitrary node and traverses its neighbors, before moving to the next level
