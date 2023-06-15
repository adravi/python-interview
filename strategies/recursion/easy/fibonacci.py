# https://www.algoexpert.io/questions/nth-fibonacci
# Fibonacci series: F(n) = F(n-1) + F(n-2)
# First fib number: 1, which means that F(1) = 0, and F(2) = 1

# input: n = 2
# output: 1 // 0, 1

# input: n = 6
# output: 5 // 0, 1, 1, 2, 3, 5

def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return getNthFib(n-1) + getNthFib(n-2)