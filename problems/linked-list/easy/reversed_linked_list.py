# https://leetcode.com/problems/reverse-linked-list/
# input: head = [1,2,3,4,5]
# output: [5,4,3,2,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prevNode = None

    while head:
        nextNode = head.next    # Save ref to the nextNode ->

        head.next = prevNode    # Connect current to previous <-
        
        prevNode = head         # Update prev
        head = nextNode         # Update current

    return prevNode     # If the while-loop broke, it means that head=None
                        # we reached the 'lastNode.next' (which is None) and must return the previous node pointer

# O(n)
# O(1)

node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
reverseList(node1)


