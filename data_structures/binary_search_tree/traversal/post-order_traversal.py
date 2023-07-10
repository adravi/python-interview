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

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    
    post_order(node.right)

    print(node.val, end=' ')

# post-order: 3 5 4 6 8 7 1

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

post_order(node1)

# theory and uses: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/