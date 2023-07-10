# https://leetcode.com/problems/same-tree/description/

# input: p = [1,2,3], q = [1,2,3]
# output: true

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):                     # DFS iterative solution using stack for comparing the 2 explored nodes in both trees
    stack = [[p, q]]                      # store the pair of nodes (p, q) in stack and perform DFS traversal
    
    while stack:
        p, q = stack.pop()                   # compare the 2 nodes, explored at the same level and position
        
        if (p and not q) or (not p and q):   # one of them being None: Trees are not the same
            return False
        
        elif p and q and p.val != q.val:     # nodes not being of equal values: Trees are not the same
            return False  

        elif p and q and p.val == q.val:     # nodes being equal: Trees are the same so far, keep exploring the trees
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])               
    
    return True

# O(n) time  // n being the number of nodes
# O(n) space // stack is extra aux memory