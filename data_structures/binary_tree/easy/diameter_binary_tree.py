class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_binary_tree(root):
    pass


# [2, 3, None, 1]
node1 = TreeNode(1)
node3 = TreeNode(3, node1)
root = TreeNode(2, node3)

print(diameter_binary_tree(root))

