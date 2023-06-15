 # This class represents a directed graph using ADJACENCY LIST representation

class Graph:
    def __init__(self): 
        self.adjacentMap = {}
 
    def addEdge(self, node1, node2):
        if node1 in self.adjacentMap:
            self.adjacentMap[node1].append(node2)
        else:
            self.adjacentMap[node1] = [node2]

        if node2 not in self.adjacentMap:
            self.adjacentMap[node2] = []

    def display(self):
        print(self.adjacentMap)

# --------------------------------------------------------------------
graph = Graph();
graph.addEdge(3, 6);
graph.addEdge(3, 9);
graph.addEdge(3, 7);
graph.addEdge(6, 11);
graph.addEdge(6, 4);
graph.addEdge(7, 1);
graph.addEdge(1, 54);
graph.addEdge(1, 2);
graph.addEdge(1, 22);

#                3
#           /    |    \
#         6      9      7
#       /  \             \
#      11   4             1
#                      /  |  \
#                    54   2   22

graph.display()

"""
IMPORTANT for AJACENCY-LIST representation:
If the graph data structure is represented as an ADJACENCY-LIST:
- Each node keeps track of all of its neighboring edges. Assume there are V nodes and E edges in the graph
- You find all of a node's neighbors by traversing its adjacency list only once in linear time
- The sum of the sizes of the adjacency lists of all nodes in a directed graph is E
    - In this example, the temporal complexity is O(V) + O(E) = O(V + E)
- Each edge in an undirected graph appears twice. Once at either end of the edge's adjacency list
    - This case's temporal complexity will be O(V) + O(2E) = O(V + E)
"""