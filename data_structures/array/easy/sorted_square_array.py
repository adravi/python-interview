# https://www.algoexpert.io/questions/sorted-squared-array
# array = [1, 2, 3, 4, 5, 6, 8, 9]

def sortedSquaredArray(array):
    squares = []

    for i in range(len(array)):
        squares.append(pow(array[i], 2))

    squares.sort()
    
    return squares

# O(n log(n)) time
# O(n) space
# ----------------------------------------------------------

def sortedSquaredArray(array):
    squares = [0] * len(array)

    leftValueIdx = 0
    rightValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):

        leftValue = array[leftValueIdx]
        rightValue = array[rightValueIdx]

        if abs(leftValue) >= abs(rightValue):
            squares[idx] = pow(leftValue, 2)
            leftValueIdx += 1
        else:
            squares[idx] = pow(rightValue, 2)
            rightValueIdx -= 1

    return squares

# O(n) time
# O(n) space