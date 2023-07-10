# https://leetcode.com/problems/diameter-of-binary-tree/
# explanation: https://www.youtube.com/watch?v=bkxqA8Rfv04&ab_channel=NeetCode

# input: see image

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# strategy is to start from bottom to top, recursively calculating the max_diameter at a given node and keep going up
def diameter_binary_tree(root):
    max_diameter = 0                # variable declared outside of the scope of inner function
    
    def dfs(node):                  # inner function: recursive DFS to find height at a given node. Problems adapts to recursion
        nonlocal max_diameter       # nonlocal: access variable declared outside of inner function
        
        if node is None:            # stop condition
            return 0
        
        left = dfs(node.left)       # recursively calculate the height of left branch 
        right = dfs(node.right)     # recursively calculate the height of right branch
        
        curr_diameter = left + right                    # at a given node, the diameter is the sum of the left and right heights
        max_diameter = max(curr_diameter, max_diameter) # update the max diameter
        
        return 1 + max(left, right) # at a given node, the height is its highest child branch height + 1 (itself)
         
    dfs(root)
    return max_diameter

# O(n) time
# O(1) space


# nonlocal: used to work with variables inside nested functions, 
#           where the variable should not belong to the inner function
#           https://www.w3schools.com/python/ref_keyword_nonlocal.asp

# [1, 2, 3, 4, 5]
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
root = TreeNode(1, node2, node3)

print(diameter_binary_tree(root))

