# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# explanation: https://www.youtube.com/watch?v=5LUXSvjmGCw&ab_channel=NeetCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""                                                This is a BST, so because of the props of it, the in-order array works
          5
        /   \
       3     6
      / \
     2   4
    /
   1

root     = [5, 3, 6, 2, 4, null, null, 1], k = 3
in-order = [1, 2, 3, 4, 5, 6] -------------------- straight-fw: generate the in-order array and return the kth element
                  ^ kth element
output   = 3 
"""
# ------------------------------------------------ iterative solution: O(k) time, O(n) space

def kth_smallest(root, k): # strat: as soon as the kth element is found, it is returned, not all the tree is traversed
    n = 0                  # maintain a counter to know when we have 'processed' the kth node
    stack = []             # iterative traversal using a stack
    curr = root            # have a pointer to the root
 
    while curr or stack:       # traversing while theres a not-null current pointer or elements in the stack
        while curr:            # advance node until we reach the end (None). 'Exploring' does NOT mean 'processing' a node
            stack.append(curr) # add element to the stack, since we want to return to this node once we exhaust the left branch
            curr = curr.left   # keep traversing the left branch of subtree

        curr = stack.pop()     # once we exhausted the left branch, pop-out the most recent element from the stack, so we process
        n += 1                 # popping an element from stack means we are 'processing' that element, so we increase n

        if n == k:             # if we found the kth element...
            return curr.val    # return the value, no need to keep exploring the tree <- OPTIMIZATION
        
        curr = curr.right      # now we explore the right branch


# ------------------------------------------------ recursive solution: O(n) time, O(1) space

def kth_smallest_rec(root, k): # this sol first generates the in-order array and returns the kth element
    def in_order_traverse(node, array):
        if node:
            in_order_traverse(node.left, array)
            array.append(node.val)
            in_order_traverse(node.right, array)
        return array
    
    res = in_order_traverse(root, [])

    return res[k-1]
        