# https://leetcode.com/problems/reorder-list/
# input: Given the 'head' of a singly linked-list:
#          (L0) → (L1) → … → (Ln - 1) → (Ln)
#        
#         re-order it as:
#          (L0) → (Ln) → (L1) → (Ln - 1) → (L2) → (Ln - 2) → …

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    slow = head
    fast = head.next

    while fast and fast.next:   # tortoise-hare strategy to reach the end of the list
        slow = slow.next        # slow -> midNode, fast -> lastNode or None (depending if the list is even)
        fast = fast.next.next


                                 # implementation of reversed linked-list
    currNode = slow.next         # reverse the second half of list, start from midNode.next (first of the second half)
    slow.next = None             # ! since we want to split the lists, the last node of first half should point to None
    
    prevNode = None              # in a revrsed-linkedlist implementation, the prev always starts as None
    while currNode:
        nextNode = currNode.next # teporarily save the next node
        currNode.next = prevNode # connect current node to the previous one <- (the one to the left)
        prevNode = currNode      # update the following previous node to be the current one, for the next iteration
        currNode = nextNode      # update the current node to the next one (tmp saved) to keep traversing the list
                                 # ! at the end of the while-loop, the prevNode is the 'head' of the reversed list


    first = head                 # first pointer on the left is simply the head (which has remained unmodified)
    second = prevNode            # second pointer (the first of the reversed-half list)
    while second:
        tmp1 = first.next        # temporarily save the next node of the first half of linked list
        tmp2 = second.next       # temporarily save the next node of the second half of linked list (which is reversed)

        first.next = second      # connect first node of 1st half of list to the second (first of 2nd half list)
        second.next = tmp1       # connect second node (first of 2nd half list) to the tmp next node of the fist list

        first = tmp1             # just update the first pointer to keep traversing the first list
        second = tmp2            # just update the second pointer to keep traversing the second list (the reversed one)

# O(2n) -> O(n) time
# O(1) space
