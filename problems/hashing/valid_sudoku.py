# https://leetcode.com/problems/valid-sudoku/

import collections

def isValidSudoku(board):
    # Sudoku board = [n]x[m] = [9]x[9]
    # The trick is identifying to which quadrant, each element belongs to.
    # ^ this is accomplished by an integer division (row//3, col//3)

    #  _____(0,0)_____       _____(0,1)_____     _____(0,2)_____
    # [0,0] [0,1] [0,2]     [0,3] [0,4] [0,5]   [0,6] [0,7] [0,8]
    # [1,0] [1,1] [1,2]     [1,3] [1,4] [1,5]   [1,6] [1,7] [1,8]
    # [2,0] [2,1] [2,2]     [2,3] [2,4] [2,5]   [2,6] [2,7] [2,8]

    #  _____(1,0)_____       _____(1,1)_____     _____(1,2)_____
    # [3,0] [3,1] [3,2]     [3,3] [3,4] [3,5]   [3,6] [3,7] [3,8]
    # [4,0] [4,1] [4,2]     [4,3] [4,4] [4,5]   [4,6] [4,7] [4,8]
    # [5,0] [5,1] [5,2]     [5,3] [5,4] [5,5]   [5,6] [5,7] [5,8]

    #  _____(2,0)_____       _____(2,1)_____     _____(2,2)_____
    # [6,0] [6,1] [6,2]     [6,3] [6,4] [6,5]   [6,6] [6,7] [6,8]
    # [7,0] [7,1] [7,2]     [7,3] [7,4] [7,5]   [7,6] [7,7] [7,8]
    # [8,0] [8,1] [8,2]     [8,3] [8,4] [8,5]   [8,6] [8,7] [8,8]

    rowsMap = [set() for _ in range(9)] # HashSet for all nums in each row
    colsMap = [set() for _ in range(9)] # HashSet for all nums in each column
    quadMap = collections.defaultdict(set) # HashMap for quadrants, where key is a tuple with quad index
                                           # {key: (row//3, col//3): set() }
    for row in range(9):
        for col in range(9):
            num = board[col][row]
            
            # Check if the value is empty ('.')
            if num == '.':
                    continue

            quadIndex = (row//3, col//3)
            if (num in rowsMap[row] or
                num in colsMap[col] or
                num in quadMap[quadIndex]):
                return False
            else:
                rowsMap[row].add(num)
                colsMap[col].add(num)
                quadMap[quadIndex].add(num)
    
    return True

# O(n^2) Time
# O(n) Space

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

isValidSudoku(board)






        

