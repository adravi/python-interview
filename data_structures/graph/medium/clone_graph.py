# https://leetcode.com/problems/clone-graph/description/
# input: see image

# explanation: https://www.youtube.com/watch?v=mQeF6bN8hMk&ab_channel=NeetCode

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# strat: maintain a map of the original nodes to cloned-ones and recursively keep cloning the neighbors
#        the cloned nodes will be appended as neighbors to each node, and thus, eventually the <-> edges will be defined
#                                                                               impotant because it is an undirected graph 
def clone_graph(root):
    if not root:
        return None # edge-case
    
    clones_map = {} # a hashmap for mapping the original nodes to clones

    def recursive_clone(node): # ----------------------------- DFS-like traversal of the graph
        if node in clones_map:
            return clones_map[node]                             # if the node already has been mapped to a clone, return it

        clone = Node(node.val)                                  # if not, create the clone
        clones_map[node] = clone                                # map the original node to the clone

        for neighbor in node.neighbors:                         # for all the adjacent nodes of each node...
            clone.neighbors.append(recursive_clone(neighbor))   # recursively clone the neighbors and append them to the clone
                                                                # this will garantee that the double edges <-> will be stablished

        return clone          # ------------------------------- # don't forget to actually return the first cloned node

    return recursive_clone(root)

# O(n) time
# O(n) space