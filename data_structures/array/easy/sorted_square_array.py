# https://www.algoexpert.io/questions/sorted-squared-array
# array = [1, 2, 3, 4, 5, 6, 8, 9]

def sorted_squared_array(array):
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

    left_val_idx = 0
    right_val_idx = len(array) - 1

    for idx in reversed(range(len(array))):

        left_val = array[left_val_idx]
        right_val = array[right_val_idx]

        if abs(left_val) >= abs(right_val):
            squares[idx] = pow(left_val, 2)
            left_val_idx += 1
        else:
            squares[idx] = pow(right_val, 2)
            right_val_idx -= 1

    return squares

# O(n) time
# O(n) space