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

    # O(1) time | O(1) space
    def setHead(self, node):
        # We are dealing with an empty list
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        # We are dealing with an empty list
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # Edge-case: We are dealing with a list of 1 node, which is the node to insert
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # We make sure to remove the nodeToInsert from the list, if it was already there
        self.remove(nodeToInsert)
        # Add the pointer references to node, before we lose them
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        # Check if the node we are inserting before of, is the head
        if node.prev is None:
            # If it was the head, update the head
            self.head = nodeToInsert
        else:
            # If it was not the head, just point the previous node to the nodeToInsert
            node.prev.next = nodeToInsert
        # Finally, connect the nodeToInsert -> node
        node.prev = nodeToInsert


    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        # Edge-case: We are dealing with a list of 1 node, which is the node to insert
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # We make sure to remove the nodeToInsert from the list, if it was already there
        self.remove(nodeToInsert)
        # Add the pointer references to node, before we lose them
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        # Check if the node we are inserting before of, is the tail
        if node.next is None:
            # If it was the tail, update the tail
            self.tail = nodeToInsert
        else:
            # If it was not the tail, just point the next node to the nodeToInsert
            node.next.prev = nodeToInsert
        # Finally, connect the node -> nodeToInsert
        node.next = nodeToInsert


    # O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        # Keep traversing until either you are the tail or you find the position
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        # You are not at the tail
        if node is not None:
            # Inser the node at the position, "replacing" the node that was in that position and pushing them ->
            self.insertBefore(node, nodeToInsert)
        # You are at the tail
        else:
            # Set the tail
            self.setTail(nodeToInsert)


    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # Copy the reference to the potential node to remove
            nodeToRemove = node
            # Update the node to keep traversing the linked list
            node = node.next
            if nodeToRemove.value == value:
                # The order of the above statements is important to not lose reference of node!
                self.remove(nodeToRemove)


    # O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)


    def removeNodeBindings(self, node):
        # Check if there is a node on the previous pointer
        if node.prev is not None:
            node.prev.next = node.next
        # Check if there is a node on the next pointer
        if node.next is not None:
            node.next.prev = node.prev
        # It is safe to update the pointers to null
        node.prev = None
        node.next = None


    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False
