# https://leetcode.com/problems/valid-parentheses/description/
# input: s = "()[]{}"
# output: True

# input: s = "(]"
# output: False

import math

def isValid(s):
    if len(s) == 0 or math.fmod(len(s), 2) != 0:
        return False
    
    stack = []
    closeToOpen = { ')': '(', ']': '[', '}': '{' }  # This makes it easier. Not rely on too may if/else

    for char in s:
        if char in closeToOpen:     # Check the keys of the map. See if a closing-parenthesis has been found
            if stack and stack[-1] == closeToOpen[char]:    # If the stack is not empty and 'peek' the top value
                stack.pop()     # If top value matches the expected open-paranthesis for the closing-one, remove it
            else:
                return False
        else:
            stack.append(char)  # If the char is not a closing-one, then it is a an opening-one 
                                # 'push' the value to the stack
            
    return len(stack) == 0  # The stack must be empty, for the string to be valid

# O(n) Time
# O(n) Space

