# https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
        1
       / \
      /   \
     /     \
    2       3
   / \      
  5  10   
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxDepth(self, root):   # recursive DFS 
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# O(V) time
# O(V + E) space  
# ------------------------------------------------------------------------

node4 = TreeNode(5)
node5 = TreeNode(10)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)

maxDepth = node1.maxDepth(node1)
print(maxDepth)
# ------------------------------------------------------------------------

#    maxDepth(1)
#
#    1 + max(maxDepth(2), maxDepth(3))
#           A               B

#           A: 1 + max(maxDepth(5), maxDepth(10))
#                          C

#           B: 1 + max(maxDepth(None, maxDepth(None))

#                   C: 1 + max(maxDepth(None, maxDepth(None))

#    1 + max(2, 1)