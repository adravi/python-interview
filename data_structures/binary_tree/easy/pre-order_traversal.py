"""
         1
       /   \
      /     \
     /       \
    4         7
   / \       / \
  3   5     6   8
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order(node):   # DFS
    if node:
        print(node.val, end=' ')
    else:
        return
    
    pre_order(node.left)
    pre_order(node.right)

# pre-order: 1 4 3 5 7 6 8

# O(V) time  / V: number of nodes
# O(1) space / the algorithm itself uses no extra aux memory
# ------------------------------------------------------------------------

node3 = TreeNode(3)
node5 = TreeNode(5)
node4 = TreeNode(4, node3, node5)
node6 = TreeNode(6)
node8 = TreeNode(8)
node7 = TreeNode(7, node6, node8)
node1 = TreeNode(1, node4, node7)

pre_order(node1)