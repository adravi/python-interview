# https://leetcode.com/problems/invert-binary-tree/
# given the root of a binary tree, invert the tree, and return its root

# input: root = [4,2,7,1,3,6,9] // pre-order listing
# output: [4,7,2,9,6,3,1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursiveInvert(self, node):
    if node:
        left = node.left
        right = node.right

        node.left = right
        node.right = left

        self.recursiveInvert(node.left)
        self.recursiveInvert(node.right)

def invertTree(self, root):
    node = root
    self.recursiveInvert(node)
    return root

# O(V) time  / V: number of vertices/nodes
# O(1) space / the algorithm itself uses no extra aux memory
