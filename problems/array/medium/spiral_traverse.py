# https://www.algoexpert.io/questions/spiral-traverse

# array dimensions size are (n * m)
# example: 4 * 4

# [0,0] [0,1] [0,2] [0,3]
# [1,0] [1,1] [1,2] [1,3]
# [2,0] [2,1] [2,2] [2,3]
# [3,0] [3,1] [3,2] [3,3]

def spiralTraverse(array):
    result = []

    # Rows
    startRow = 0
    # (n - 1) = 3
    endRow = len(array) - 1

    # Columns
    startCol = 0
    # (m - 1) = 3
    endCol = len(array[0]) - 1

    # Because we defined the endRow and endCol as (dimensionSize - 1), we want to include the borders
    while startRow <= endRow and startCol <= endCol:
        # Remember the range(x) function does not include x !

        # [0.0] [0,1] [0,2] [0,3]
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # Check if array has a single row
        if startRow == endRow:
            break

        # [1,3] [2,3] [3,3]
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # Check if array has a single col
        if startCol == endCol:
            break
            
        # [3,2] [3,1] [3,0]
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

        # [2,0] [1,0]
        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

        # Update row start and end -> Reduce the rectanlge to travel inwards
        startRow += 1
        endRow -= 1
        # Update col start and end -> Reduce the rectanlge to travel inwards
        startCol += 1
        endCol -= 1

    return result

# O(n * m) Time -> or O(m) if single row, or O(n) if single column
# O[n * m] Space

        