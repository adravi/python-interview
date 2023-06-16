# Depth First Search
# Iterative using a stack in a graph represented as an adjacency list

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

    def DFS(self, rootNode):
        stack = [rootNode]
        visited = set()        # the hash-set is to avoid visiting a node more than once. be aware, there could be CYCLES

        while stack:
            node = stack.pop()
            print(node, end=' ')
            
            visited.add(node)  # mark the node as visited

            for adjacentNode in self.adjacentMap[node]: # get all adjacent nodes of the popped node
                if adjacentNode not in visited:         # if a adjacent hasn't been visited, push it to stack
                    stack.append(adjacentNode)

#   O(n) time  / the algo itself only visits each node once
#   O(n) space / the set and stack can store all the vertices, each O(2n) -> O(n)

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

graph = Graph();
graph.addEdge(3, 7);
graph.addEdge(3, 9);
graph.addEdge(3, 6);
graph.addEdge(6, 4);
graph.addEdge(6, 11);
graph.addEdge(7, 1);
graph.addEdge(1, 22);
graph.addEdge(1, 2);
graph.addEdge(1, 54);

#                3
#           /    |    \
#         6      9      7
#       /  \             \
#      11   4             1
#                      /  |  \
#                    54   2   22


# DFS: 3, 6, 11, 4, 9, 7, 1, 54, 2, 22 | traverse order is RIGHT LEFT: <-

graph.DFS(3)