# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head (see input image)
# input: head = [1,2,3,4,5], n = 2
# output: [1,2,3,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# we need to find the node, previous to the one we wish to remove (so we can update its pointers to skip the undisired)

#  slow                        fast
#  dummy      head
#  (-1)   ->   (1)  ->  (2)  -> (3)  ->  (4)  -> (5) -> None
#            ^----- n -----^

# strategy is to have 2 pointers. slow -> dummyNode (one before the head) and fast(separated by n nodes in between)
# then we keep moving the 2 pointers to the right, 1 position at a time

#                               slow                     fast
#  (-1)   ->   (1)  ->  (2)  -> (3)  ->  (4)  -> (5)  -> None
#                                      ^----- n -----^

# by the time the fast pointer reaches None, slow pointer will be at node that is previous to the to-be-removed node 
def removeNthFromEnd(head, n):
    dummyNode = ListNode(-1, head)
    slow = dummyNode            # slow = dummyNode (one before the head)
    fast = head                 # fast = head

    for i in range(n):
        if fast:
            fast = fast.next     # shift fast to be separated from slow by n nodes in between

    while fast:
        slow = slow.next         # traverse list, one position at a time
        fast = fast.next

    if slow.next:
        slow.next = slow.next.next # connect the node, at slow pointer, to the next.next one (to skip next, the undisired)

    return dummyNode.next        # dummy still points to head, just return it


    
