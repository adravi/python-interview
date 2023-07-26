# https://leetcode.com/problems/invert-binary-tree/
# given the root of a binary tree, invert the tree, and return its root

# input: root = [4,2,7,1,3,6,9] // pre-order listing
# output: [4,7,2,9,6,3,1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursive_invert(self, node):
    if node:
        left = node.left
        right = node.right

        node.left = right
        node.right = left

        self.recursive_invert(node.left)
        self.recursive_invert(node.right)

def invert_tree(self, root):
    node = root
    self.recursive_invert(node)
    return root

# O(V) time  / V: number of vertices/nodes
# O(1) space / the algorithm itself uses no extra aux memory
