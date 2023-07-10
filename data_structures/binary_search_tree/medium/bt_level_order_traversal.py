# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (from left to right, level by level)
"""
input: root = [3, 9, 20, null, null, 15, 7]

         3
      /     \
     /       \
    9         20
             / \
            15   7

output: [[3],[9,20],[15,7]]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def level_order(root):
    if not root:
        return []
    
    queue =  deque([root])
    res = []

    while queue:
        level_size = len(queue) # number of elements on that level
        temp = []               # list to store all the left and right child for all the node in the same level

        while level_size > 0:
            node = queue.popleft()          # Dequeue node from queue
            temp.append(node.val)           # Store the value of node to temp
            
            if node.left:                   # Store all the nodes of next level
                queue.append(node.left)
            if node.right:                  # Add left and right child (if any)
                queue.append(node.right)

            level_size -= 1
        
        res.append(temp) # Add the temp to output result...
    
    return res

# O(n) time
# O(n) space