# https://leetcode.com/problems/clone-graph/description/

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(self, root):
    if not root:
        return None
    
    clones_map = {}

    def recursive_clone(node):
        if node in clones_map:
            return clones_map[node]

        clone = Node(node.val)
        clones_map[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(recursive_clone(neighbor))

        return clone

    return recursive_clone(root)