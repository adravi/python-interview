# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Lowest Common Ancestor: It's defined between two nodes p and q as the lowest node in T 
#                         that has both p and q as descendants (where we allow a node to be a descendant of itself)

# explanation: https://www.youtube.com/watch?v=gs2LMfuOR9k&ab_channel=NeetCode

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# if there is a split between 2 nodes, thats the LCA
# if you find one of the nodes itself, then thats the LCA, because no other node will be the ancestor of that one 
#    (assume the other exists in some subtree) The problem assures the 2 nodes p and q exists
def lowest_common_ancestor(root, p, q):
    curr = root

    while curr:
        if curr.val > p.val and curr.val > q.val:
            curr = curr.left

        elif curr.val < p.val and curr.val < q.val:
            curr = curr.right

        else:
            return curr


# O(log(n)) time
# O(1)      space