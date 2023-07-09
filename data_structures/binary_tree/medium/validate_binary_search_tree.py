# https://leetcode.com/problems/validate-binary-search-tree/

# explanation: https://www.youtube.com/watch?v=s6ATEkipzow&ab_channel=NeetCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    # DFS recursive traversal adapts naturally
    def valid_subtree(left_bound, node, right_bound):
        if not node:
            return True
        
        if left_bound < node.val < right_bound:
            return (valid_subtree(left_bound, node.left, node.val) and
                    valid_subtree(node.val, node.right, right_bound))
        else:
            return False
        
    valid_subtree(float('-inf'), root, float('inf'))
