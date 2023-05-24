# https://www.algoexpert.io/questions/remove-duplicates-from-linked-list

# input: linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1
# output: 1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList

    while currentNode is not None:
        nextDistinctNode = currentNode.next

        # Inspect if the next node has the same value as the current (if there is one, at all)
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = currentNode.next

    return linkedList

# O(n) T
# O(1) S
