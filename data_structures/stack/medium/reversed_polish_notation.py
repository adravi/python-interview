# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# input: ["2","1","+","3","*"]
# output: 9 // ((2 + 1) * 3)

# input: ["4","13","5","/","+"]
# output: 6 // (4 + (13 / 5))

# Trick is to push numbers into stack until finding a sign
# When finding a sign, pop the previous 2 tokens and execute the operation, then push result to the stack (new term)
def evalRPN(tokens):
    stack = []

    # Be careful on how you pop() nums a and b! The problem indicates the order of how ops must be executed
    for token in tokens:
        if token == '+':    # newTerm -> b + a
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif token == '-':  # newTerm -> b - a
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == '*':  # newTerm -> b * a
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif token == '/':  # newTerm -> b / a  IMPORTANT!: Make sure to use a division towards zero
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))    #                   int(decimal division) -> int(b/a)
        else:
            stack.append(int(token))

    return stack.pop()

# O(n) Time
# O(n) Space

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

# (a / b)     -> Decimal division
# (a // b)    -> Integer division, rounded down
# int(a / b)  -> Integer division, towards zero