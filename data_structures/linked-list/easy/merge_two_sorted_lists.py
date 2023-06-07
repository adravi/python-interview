# https://leetcode.com/problems/merge-two-sorted-lists/
# input: list1 = [1,2,4], list2 = [1,3,4]
# output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# We don't actually build a new list, we create a set of pointers to the right node of the 2 lists
def mergeTwoLists(self, list1, list2):
    dummyHead = ListNode()  # Have a dummy-head, to avoid the edge-case of inserting a next node on an empty list
    tail = dummyHead        # The trick is having the tail point to the next ordered node

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next # Either way, we move the pointer of the list

    if list1:   # Make sure to attach the rest of whichever list that hasn't been fully traversed
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummyHead.next   # The dummy-head's tail is the actual merged list

# O(n + m) Time -> The size of the 2 lists
# O(1) Space

#--------------------------------------------------------------------------------------------------------
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# dummy ->
# ^ tail

# 1 < 1: tail.next = [1, 2, 4] list1 // list1 will point to the next node in list1
#                     ^ 

# 2 > 1: tail.next = [1, 3, 4] list2 // list2 will point to the next node in list2
#                     ^
