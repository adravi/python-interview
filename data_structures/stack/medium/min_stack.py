# https://leetcode.com/problems/min-stack/
# Methods pop(), top() and getMin() methods will always be called on non-empty stacks

"""
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""

def __init__(self):                # the key is maintaining 2 arrays 
    self.stack = []                # one for actually storing the values as they come. easily pointing at the last one
    self.min_stack = []            # one for updating what is the minimum value, at the moment after 'pushing' a new value

def push(self, val: int) -> None:
    self.stack.append(val)                                             # just append the new value
    minimum = min(val, self.min_stack[-1] if self.min_stack else val)  # compare the new value to the current minimum (if any)
    self.min_stack.append(minimum)                                     # append the minimum to the min_stack, its ok to repeat

def pop(self) -> None:
    self.stack.pop()      # just pop() out the last one
    self.min_stack.pop()  # also pop() out the last one, so the last one becomes what was the min, after inserting the previous

def top(self) -> int:
    return self.stack[-1]       # return the last one of the actual stack, but don't pop anything

def getMin(self) -> int:
    return self.min_stack[-1]   # return the current minimum (the lastly calculated min, after inserting the most recent val)
                                # but dont pop() out anything
    
# O(1) time  // each operation
# O(n) space