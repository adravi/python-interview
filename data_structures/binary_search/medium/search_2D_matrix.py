# https://www.youtube.com/watch?v=Ber2pi2C0j0&ab_channel=NeetCode
# input: [ [ 1, 3, 5, 7]    
#          [10,11,16,20]    <- matrix[n][m], target = 3
#          [23,30,34,60] ]
# output: True

# Execute a BS first to locate the row (by using the extreme values), and then execute BS on the nums of that row
def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    rowInRange = -1   # the row in which range, the target could exist

    topRow = 0
    bottomRow = rows - 1
    while topRow <= bottomRow:              # an implementation of BS for searching the rowInRange
        midRow = (topRow + bottomRow) // 2

        if target < matrix[midRow][0]:
            bottomRow = midRow - 1

        elif target > matrix[midRow][-1]:
            topRow = midRow + 1

        else: # matrix[midRow][0] < target < matrix[midRow][-1]
            rowInRange = midRow
            break

    if rowInRange  == -1:# if the rowInRange was never assigned, the while-loop ended without fidning a potential row
        return False

    left = 0
    right = cols - 1
    while left <= right:                    # a classic implementation of BS
        mid = (left + right) // 2

        if target < matrix[rowInRange][mid]:
            right = mid - 1

        elif target > matrix[rowInRange][mid]:
            left = mid + 1

        else:
            return True
        
    return False

# O(log(n) + log(m)) -> O(log(n + m))
# O(1)

searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
