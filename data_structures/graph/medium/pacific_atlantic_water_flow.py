# https://leetcode.com/problems/pacific-atlantic-water-flow/
# input: see image
# explanation: https://www.youtube.com/watch?v=s-VkcjHqkGI&ab_channel=NeetCode

# through DFS:
#   inspect first row (top) and first column (left) for PACIFIC, the heights must be non-increasing to be flow-valid
#   inspect last row (bottom) and last column (right) for ATLANTIC, the heights must be non-increasing to be flow-valid

def pacific_atlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])       # as always, define the dimensions of the grid, from the beggining
    visited_pacific, visited_atlantic = set(), set() # have 2 hashsets, 1 for each ocean, to store the visited coordinates


    def dfs(r, c, visited, prev_height): # -------------------------- DFS internal function
        if (r not in range(ROWS) or
            c not in range(COLS) or               # check if the position coordinates are in-bound with the grid dimensions
            (r, c) in visited or                  # check if the position has been visited already
            heights[r][c] < prev_height):         # check if curr height is lower than the previous height (water doesnt flow)
            return                                # if any of the above is true, then this position must not be 'processed' next
        
        visited.add((r, c))                       # if not, then this position is 'processed' and must be marked as visited

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]] # the directions of the next 4 ceil positions to inspect in the grid
        for dir_r, dir_c in dirs:
            new_pos_r = r + dir_r                             # update the position of row and cols
            new_pos_c = c + dir_c
            dfs(new_pos_r, new_pos_c, visited, heights[r][c]) # recursively call DFS on each of the next positions to inspect
                                                              # the current position (r, c) is passed as the prev_position
    

    for col in range(COLS):                                       # go to every column in the first row | flow into pacific                                                 
        dfs(0, col, visited_pacific, heights[0][col])             # \/ expand ceils top-to-bottom | must be non-increase

        dfs(ROWS-1, col, visited_atlantic, heights[ROWS-1][col])  # go to every row in the last column | flow into atlantic
                                                                  # ^ expamd ceils bottom-to-top | must be non-increase

    for row in range(ROWS):                                       # go to every row in the first column | flow into pacific
        dfs(row, 0, visited_pacific, heights[row][0])             # -> expand ceils left-to-right | must be non-increase

        dfs(row, COLS-1, visited_atlantic, heights[row][COLS-1] ) # go to every column in the last row | flow into atlantic
                                                                  # <- expand ceils right-to-left | must be non-increase

    res = []
    for row in range(ROWS):                        # Finally, inspect every ceil on the grid
        for col in range(COLS):
            if ((row, col) in visited_pacific and
                (row, col) in visited_atlantic):
                res.append([row, col])             # if the position appears in both pacif and atlan sets, it's part of result

    return res

# O(m x n) time  // size of the grid
# O(1)    space  // recursive algorithm
