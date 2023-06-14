# https://www.algoexpert.io/questions/branch-sums
"""
         1
       /   \
      /     \
     /       \
    2         3
   / \       / \
  5  10     7   8

output: [8, 13, 11, 12]
"""

class BinaryTree:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs_recursive(node, sum, sumList):
    sum += node.value       # update the running sum

    if not node.left and not node.right:    # you have reached a leave node!
        sumList.append(sum)                 # append the branch sum and return
        return
    
    if node.left:   
        dfs_recursive(node.left, sum, sumList) # if there's left child, call recursive with updated sum to keep traversing tree
    if node.right:
        dfs_recursive(node.right, sum, sumList) # if there's left child, call recursive with updated sum to keep traversing tree

def branchSums(root):
    sumList = []
    sum = 0
    dfs_recursive(root, sum, sumList)
    return sumList