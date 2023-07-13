# https://leetcode.com/problems/pacific-atlantic-water-flow/
# input: see image

# explanation: https://www.youtube.com/watch?v=s-VkcjHqkGI&ab_channel=NeetCode

def pacific_atlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    visited_pacific, visited_atlantic = set(), set()

    def dfs(r, c, visited, prev_height):
        if (r not in range(ROWS) or
            c not in range(COLS) or
            (r, c) in visited or
            heights[r][c] < prev_height):
            return
        
        visited.add((r, c))
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dir_r, dir_c in dirs:
            new_pos_r, new_pos_c = (r + dir_r), (c + dir_c)
            dfs(new_pos_r, new_pos_c, visited, heights[r][c])
        
    for col in range(COLS):
        prev_height_pacific = heights[0][col]                      # Go to every column in the first row
        dfs(0, col, visited_pacific, prev_height_pacific)          # pacific ->  | flowing to the right from pacific    

        prev_height_atlantic = heights[ROWS-1][col]                # Go to every column in the last row
        dfs(ROWS-1, col, visited_atlantic, prev_height_atlantic)   # <- atlantic | flowing to the left from atlantic

    for row in range(ROWS):
        prev_height_pacific = heights[row][0]                      # Go to every row in the first column
        dfs(row, 0, visited_pacific, prev_height_pacific)          # \/ pacific  | flowing to the bottom from pacific

        prev_height_atlantic = heights[row][COLS-1]                # Go to every row in the last column
        dfs(row, COLS-1, visited_atlantic, prev_height_atlantic)   # ^ atlantic  | flowing to the top from atlantic

    res = []
    for row in range(ROWS):
        for col in range(COLS):
            if ((row, col) in visited_pacific and
                (row, col) in visited_atlantic):
                res.append([row, col])

    return res
