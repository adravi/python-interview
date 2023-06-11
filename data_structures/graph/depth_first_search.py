# Depth First Search
# Iterative using a stack

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
        visited = set()

        while stack:
            node = stack.pop()
            print(node, end=' ')
            
            visited.add(node)  # mark the node as visited

            for adjacentNode in self.adjacentMap[node]: # get all adjacent nodes of the popped node
                if adjacentNode not in visited:         # if a adjacent hasn't been visited, push it to stack
                    stack.append(adjacentNode)


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

# O(V + E) time
# O(V) space | aux memory: set()