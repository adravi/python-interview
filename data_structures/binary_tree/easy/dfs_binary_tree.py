class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if root:
        print(root.val, end=" ")
    else:
        return

    dfs(root.left)
    dfs(root.right)

"""
         1
       /   \
      /     \
     /       \
    2         3
   / \       / \
  5  10     7   8
"""

node4 = BinaryTree(5)
node5 = BinaryTree(10)
node2 = BinaryTree(2, node4, node5)
node31 = BinaryTree(7)
node32 = BinaryTree(8)
node3 = BinaryTree(3, node31, node32)
node1 = BinaryTree(1, node2, node3)

dfs(node1)