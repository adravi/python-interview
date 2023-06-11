#                                        FIRST K ELEMENTS
# array = [2, 7, 3, 4, 5, 6]
# k = 3
# print(array[:k])
# --------------------------------------

#                                       ENUMERATE: i,v = index, value
# string = 'hsbfmssa'
# for i, char in enumerate(string):
#     print(i, char)

# --------------------------------------
#                                       ORD(): get ASCI value of char
# char = 'a'
# charValue = ord(char)
# print(charValue + 1)
# print(ord('b'))

# --------------------------------------

#                                       QUEUE
# from collections import deque

# myQueue = deque()

# myQueue.append(1)
# myQueue.append(2)
# myQueue.append(3)
# myQueue.append(4)

# print(myQueue)

# print('Dequeue element')
# myQueue.popleft()
# print(myQueue)

# print('See FIRST inserted element')
# print(myQueue[0])

# print('See LAST inserted element')
# print(myQueue[-1])

# --------------------------------------

stack = []
stack.append(3)
stack.append(4)
print(stack)

n1 = stack.pop()
if stack:
    print(stack)
else:
    print('stack is empty')

n2 = stack.pop()
if stack:
    print(stack)
else:
    print('stack is empty')