# https://leetcode.com/problems/copy-list-with-random-pointer/
# input: see image

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# strat: Two passes, one for the copy-nodes creation, a 2nd one for the linking. Have a hashmap for accessing 
def copy_random_list(head):
    copies = { None: None }   # have a (key:pair) element pointing to None, for edge cases of random pointing to None

    curr = head               # set the current node to the beginning of the list
    while curr:
        copy = Node(curr.val)           # create the copy-node
        copies[curr] = copy             # store the ref to the copy-node in the hashmap, using the curr node as key
        curr = curr.next                # keep exploring the list

    curr = head               # reset the current node to the beginning of the list
    while curr:
        copy = copies[curr]               # access the copy-node using the hashmap, and the curr node as key
        copy.next = copies[curr.next]     # get next node by simply using curr.next as key, since all the copy-nodes are accessible
        copy.random = copies[curr.random] # get random node by using curr.random as key, since all the copy-nodes are accessible
        curr = curr.next                  # keep exploring the list

    return copies[head]     # simply return the head by getting it from the map, since all the copy-nodes are accessible

# O(n) time  // O(2n) -> O(n)
# O(n) space // hashmap aux mem