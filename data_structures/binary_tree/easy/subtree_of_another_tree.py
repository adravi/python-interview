# https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(self, root, subRoot):
    def isSameTree(p, q):
        stack = [[p, q]]

        while stack:
            p, q = stack.pop()

            if (p and not q) or (not p and q):
                return False

            elif p and q and p.val != q.val:
                return False

            elif p and q and p.val == q.val:
                stack.append([p.left, q.left])
                stack.append([p.right, q.right])               
        
        return True
    
    isSubTree = False

    def dfs(node):
        nonlocal isSubTree

        if not node:
            return
        
        if node.val == subRoot.val:
            if isSameTree(node, subRoot):
                isSubTree = True
                return
        
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return isSubTree