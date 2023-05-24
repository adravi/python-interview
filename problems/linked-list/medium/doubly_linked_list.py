# https://www.algoexpert.io/questions/linked-list-construction

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        self.head = node

    def setTail(self, node):
        self.tail = node

    def insertBefore(self, node, nodeToInsert):
        currentNode = self.head
        while currentNode:
            nextNode = currentNode.next
            if nextNode.value == node.value:
                currentNode.next = nodeToInsert
                nodeToInsert.next = nextNode
            currentNode = nextNode

    def insertAfter(self, node, nodeToInsert):
        currentNode = self.head
        while currentNode:
            nextNode = currentNode.next
            if currentNode.value == node.value:
                currentNode.next = nodeToInsert
                nodeToInsert.next = nextNode
            currentNode = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass
