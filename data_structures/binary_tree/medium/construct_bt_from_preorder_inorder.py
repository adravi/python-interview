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

# strat: find the root in 'preorder', then locate the root in 'inorder', (the new root of a subtree is in the middle)
#        then RECURSIVELY call the function with the 'trimmed' sublists, the left one represents the left sublist and so on...
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(root.val)   # [9, 3, 15, 20, 7]
                                    #     ^
                                    #    mid
                                    # the left sublist represents the left subarray, and the right sublist the right subarray

    root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])   # preorder: [not-include first one (root) : mid]
                                                                   #                                  (right is not inclusive)
                                                                   # inorder: [everything up to (mid-1)]

    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:]) # preorder: [everything from one after the mid]
                                                                   # inprder: [everything from mid+1]

    return root

# O(log n) time
# O(1) space




