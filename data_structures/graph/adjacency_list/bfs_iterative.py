# Breadth First Search
# Iterative using a queue a graph represented as an adjacency list

from collections import deque

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

    def BFS(self, rootNode):
        queue = deque()
        queue.append(rootNode)
        visited = set()

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            visited.add(node)   # mark the node as visited
 
            for adjacentNode in self.adjacentMap[node]: # get all adjacent vertices of the dequeued node
                if adjacentNode not in visited: # if an adjacent hasn't been visited, mark it visited and enqueue it
                    queue.append(adjacentNode)

# O(V) time
# O(V + E) space | aux memory: set()

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


# BFS: 3, 6, 9, 7, 11, 4, 1, 54, 2, 22

graph.BFS(3)