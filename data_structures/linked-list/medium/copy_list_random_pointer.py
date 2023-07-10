# https://leetcode.com/problems/copy-list-with-random-pointer/


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head):
    copies = { None: None }

    curr = head
    while curr:
        copy = Node(curr.val)
        copies[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        copy = copies[curr]
        copy.next = copies[curr.next]
        copy.random = copies[curr.random]
        curr = curr.next

    return copies[head]