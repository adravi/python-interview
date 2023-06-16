# https://leetcode.com/problems/same-tree/description/

# input: p = [1,2,3], q = [1,2,3]
# output: true

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):                     # DFS iterative solution using stack
    stack = [[p, q]]                      # store the pair of nodes (p, q) in stack and perform DFS traversal
    
    while stack:
        p, q = stack.pop()
        
        if p and q and p.val == q.val:    # p, q, being equal
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])

        # (not p and not q)               # another true case

        elif p or q:                      # the negation of it ^ is: (p or q) by DeMorgan's law
            return False                  # this could be understood at either only p or q being None
    
    return True

# O(n) time  // n being the number of nodes
# O(n) space // stack is extra aux memory