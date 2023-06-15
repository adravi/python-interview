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
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    
    print(node.val, end=' ')
    
    in_order(node.right)

# post-order: 3 4 5 1 6 7 8

# O(V) time  / V: number of vertices/nodes
# O(1) space / algo does not use extra aux memory
# ------------------------------------------------------------------------

node3 = TreeNode(3)
node5 = TreeNode(5)
node4 = TreeNode(4, node3, node5)
node6 = TreeNode(6)
node8 = TreeNode(8)
node7 = TreeNode(7, node6, node8)
node1 = TreeNode(1, node4, node7)

in_order(node1)