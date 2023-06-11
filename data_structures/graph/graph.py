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