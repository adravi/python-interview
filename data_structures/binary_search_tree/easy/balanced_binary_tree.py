# https://leetcode.com/problems/balanced-binary-tree/description/

# input: root = [3,9,20,null,null,15,7]
# output: true
"""
        3
      /   \
    9      20
          /  \
        15    7
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):

    def dfs(node):      # have an internal function dfs() that will return a composite value: 
                        # [are the left and right subtrees balanced?, height of current tree]
        if not node:
            return [True, 0]
        
        heightLeft = dfs(node.left)   # recursively call dfs() with left
        heightRight = dfs(node.right) # recursively call dfs() with right

        balanced = (heightLeft[0] and heightRight[0] and       # a tree is balanced if its left and right subtrees are balanced
                    abs(heightLeft[1] - heightRight[1]) <= 1)  # and if the height of subtrees dont differ by more than 1

        return [balanced, 1 + max(heightLeft[1], heightRight[1])] # return composite val [balanced, height: max subtree height]
                                                                  # max subtree height: max(heightLeft, heightRight)
    
    isTreeBalanced = dfs(root)[0]
    return isTreeBalanced

# O(n) time (n: number of nodes)
# O(1) space
