# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

"""
        3
      /   \
    9      20
          /  \
        15    7

input:
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

output: [3, 9, 20, null, null, 15, 7]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)   # [9, 3, 15, 20, 7]
                                    #     ^
                                    #    mid

    root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])

    return root




