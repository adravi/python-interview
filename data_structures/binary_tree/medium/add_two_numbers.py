# https://leetcode.com/problems/add-two-numbers

# input: l1 = [2,4,3], l2 = [5,6,4]   // see input image 
# output: [7,0,8] //  342 + 465 = 807

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(p, q):
        dummyHead = ListNode(-1)           # strategy of dummy head, to have an initial pointer to start (and eventually return)
        carry = 0
        curr = dummyHead
        
        while p or q:
            x = p.val if p else 0         # it could be that one of the nodes is None
            y = q.val if q else 0

            sum = x + y + carry            # the carry is very important!
            carry = sum // 10

            curr.next = ListNode(sum % 10) # update pointers of the result
            curr = curr.next

            if p:                          # keep traversing the linked lists (if theres any next node) 
                p = p.next
            if q:
                q = q.next
        
        if carry > 0:                      # if there was a carry at the very end, a new Node must be created
            curr.next = ListNode(carry)

        return dummyHead.next              # return everything after the dummy head

# O(n) time
# O(1) space