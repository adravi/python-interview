# https://leetcode.com/problems/middle-of-the-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        if not head:
            return head
        
        slow = head
        fast = head.next

        while fast:
            slow = slow.next
            
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        
        return slow

# O(n) time
# O(1) space