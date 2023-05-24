# https://www.algoexpert.io/questions/middle-node

# input: linkedList = 2 -> 7 -> 3 -> 5
# output: 3 -> 5 // Node with value 3

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode(linkedList):
    # Have a fast pointer moving twice as fast as the slow pointer
    slowNode = linkedList
    fastNode = linkedList

    # The traversal ends when the fast pointer is pointing to null
    while fastNode and fastNode.next:
        slowNode = slowNode.next

        # We know for sure that at least fastNode.next is not None
        fastNode = fastNode.next.next
            
    # By the time the fastPointer reached the end of the list,
    # the slowPointer should be pointing at the middle node (already to the second number, if the list is even)
    return slowNode

# O(n) T
# O(1) S

# -------------------------------------------------------------------------------------
# Edge-case: List containing only 2 nodes -> The first node is considered the middle-node
# 1 -> 2