# https://www.algoexpert.io/questions/find-closest-value-in-bst
# input & output : see .png file

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    node = tree
    closestNum = -1
    smallestDiff = float('inf')
    
    while node:
        diff = abs(node.value - target)

        if diff < smallestDiff:     # Compare diff between current node and target
            smallestDiff = diff     # Update variable holding the closest node and the diff between it and the target
            closestNum = node.value
        
        if target < node.value:     # If the target is smaller than current value, explore the left side
            node = node.left        # look for smaller values

        elif target > node.value:   # If the target is greater than current value, explore the right side
            node = node.right       # look for larger values

        else: # diff = 0
            return node.value       # if the target and the curent node have the same value, return it
                                    # there wont be a smaller diff than zero!
    return closestNum

