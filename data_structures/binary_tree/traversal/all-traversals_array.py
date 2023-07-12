# https://www.algoexpert.io/questions/bst-traversal

# theory and uses: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

def pre_order_traverse(tree, array):
    if tree:
        array.append(tree.value)
        pre_order_traverse(tree.left, array)
        pre_order_traverse(tree.right, array)
    return array

def in_order_traverse(tree, array):
    if tree:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array

def post_order_traverse(tree, array):
    if tree:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)
    return array