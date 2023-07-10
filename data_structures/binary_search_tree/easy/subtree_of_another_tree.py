# https://leetcode.com/problems/subtree-of-another-tree/
# input: tree of size T, subtree of size S

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# strategy: recursively explore the tree, 
#           for any node matching the root of subtree recursively explore the rest of the tree to see if they match entirely
def is_subtree(tree, subtree):
    if not subtree:              # any empty subtree is encompased in any given tree (even if the tree is empty)
        return True
    if not tree:                 # if a tree is empty, no non-empty subtree will be encompased in it
        return False
    
    if same_tree(tree, subtree): # we know that tree and subtree are non-empty. Make the comparison starting from the roots
        return True
    
    return (is_subtree(tree.left, subtree) or     # keep exploring to see if at least, one of the branches is the same
            is_subtree(tree.right, subtree))


def same_tree(t1, t2):            # helper function      
    if not t1 and not t2:         # if both the tree nodes are empty, we can call them "the same"
        return True
    
    if t1 and t2 and t1.val == t2.val:           # if the tree nodes are non-empty, compare their values
        return (same_tree(t1.left, t2.left) and  # keep exploring to see if at least, one of the branches is the same
                same_tree(t1.right, t2.right))
    
    return False                                 # if we reach this point, the trees are NOT the same

# O(T * S) time
# O(1)     space
