# Depth First Search
# Recursive in a graph represented as an adjacency list

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


    def DFS(self, node, visited):        
        print(node, end=' ')
        visited.add(node)    # The hashset is to avoid visiting each node more than once. The graph could have cycles!

        for adjacentNode in self.adjacentMap[node]:
            if adjacentNode not in visited:
                self.DFS(adjacentNode, visited)

"""
If the entire graph is traversed, the temporal complexity of DFS is O(V), where V is the number of vertices.
"""

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
#       /  \   /         \
#      11   4             1
#                      /  |  \
#                    54   2 - 22        GRAPH HAS CYCLES!

graph.DFS(3, set())