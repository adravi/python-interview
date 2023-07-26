# Depth First Search
# Recursive in a graph represented as an adjacency list

class Graph:
    def __init__(self): 
        self.adjacent_map = {}
 
    def add_edge(self, node1, node2):
        if node1 in self.adjacent_map:
            self.adjacent_map[node1].append(node2)
        else:
            self.adjacent_map[node1] = [node2]

        if node2 not in self.adjacent_map:
            self.adjacent_map[node2] = []


    def DFS(self, node, visited):        
        print(node, end=' ')
        visited.add(node)    # The hashset is to avoid visiting each node more than once. The graph could have cycles!

        for adjacentNode in self.adjacent_map[node]:
            if adjacentNode not in visited:
                self.DFS(adjacentNode, visited)

"""
If the entire graph is traversed, the temporal complexity of DFS is O(V), where V is the number of vertices.
"""

graph = Graph();
graph.add_edge(3, 6);
graph.add_edge(3, 9);
graph.add_edge(3, 7);
graph.add_edge(6, 11);
graph.add_edge(6, 4);
graph.add_edge(7, 1);
graph.add_edge(1, 54);
graph.add_edge(1, 2);
graph.add_edge(1, 22);

#                3
#           /    |    \
#         6      9      7
#       /  \   /         \
#      11   4             1
#                      /  |  \
#                    54   2 - 22        GRAPH HAS CYCLES!

graph.DFS(3, set())