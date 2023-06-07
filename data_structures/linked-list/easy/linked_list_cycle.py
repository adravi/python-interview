# https://leetcode.com/problems/linked-list-cycle/description/
# input: head = [3, 2, 0, -4]// pos = 1 // 3 -> 2 -> 0 -> -4 -> 2
#                               There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).                                            
# output: true

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# solution using hash-set
def hasCycle(head):
        valSet = set()

        while head and head not in valSet:
            valSet.add(head)
            head = head.next

        if head:
            return True
        else:
            return False
        
# O(n) time
# O(n) space // aux memory: hash-set with pointers as elements

# ---------------------------------------------------------------------------------------------------

# solution using tortoise-hare strategy
def hasCycle(head):
     pass