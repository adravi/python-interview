# https://leetcode.com/problems/max-area-of-island/
# input: see image
# explanation: https://www.youtube.com/watch?v=iJGr1OtmH0c&ab_channel=NeetCode


# recursive DFS to expand the ceils (nodes) of each connected component of the graph (repesented as a matrix)
def max_area_of_island(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visited  = set()

    def dfs(r, c):                   # internal function - recursive DFS
        if (r not in range(ROWS) or  # check if the row ceil is out of range
            c not in range(COLS) or  # check if the column ceil is out of range
            grid[r][c] == 0 or       # check if the ceil value is 'water' (no more land)
            (r, c) in visited):      # check if this ceil has already been visited and thus, considered as part of another island
            return 0                 # in this case, return 0, no more pieces of land to count
        
        visited.add((r, c))          # if not, this ceil indeed is a piece of land and must be marked as visited

        return (1 + dfs(r + 1, c) +  # count the already found piece of land (+1) and recursively keep exploring the 
                    dfs(r - 1, c) +  # 4 ceils (left, right, above, underneath) that can have another connected piece of land
                    dfs(r, c + 1) +
                    dfs(r, c - 1))
    
    max_area = 0
    for r in range(ROWS):                        # simply traverse all the ceils in the grid
        for c in range(COLS):
            max_area = max(max_area, dfs(r, c))  # update the max area, we can simply call the recursive DFS on each ceil

    return max_area


# O(n) time  // where n is the ROWS * COLUMNS - we explore the whole grid
# O(1) space // no extra memory is used

# ----------------------------------------------------------------------------------- DFS using stack (see number_of_islands)
def max_area_of_island_dfs(grid):
    if not grid: return 0

    ROWS, COLS = len(grid), len(grid[0])
    visited  = set()
    max_area = 0

    def dfs(r, c):          # DFS using stack
        stack = [(r, c)]    # stack, as normal with iterative DFS
        visited.add((r, c)) # each element will be a pair of the coordenates (row, column)
        area = 1

        while stack:
            pos_r, pos_c = stack.pop()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dir_r, dir_c in directions:
                check_r = pos_r + dir_r         # new position to check, with the direction applied
                check_c = pos_c + dir_c         # new position to check, with the direction applied
                
                if (check_r in range(ROWS) and
                    check_c in range(COLS) and
                    grid[check_r][check_c] == 1 and
                    (check_r, check_c) not in visited):
                    stack.append((check_r, check_c))
                    visited.add((check_r, check_c))
                    area += 1
            
        return area

    for r in range(ROWS):
        for c in range(COLS):
            if (grid[r][c] == 1 and
                (r, c) not in visited):
                island_area = dfs(r, c)
                max_area = max(island_area, max_area)

    return max_area


# ----------------------------------------------------------------------------------- BFS using queue (see number_of_islands)
from collections import deque

def max_area_of_island_bfs(grid):
    if not grid: return 0

    rows, cols = len(grid), len(grid[0])
    visited  = set()
    max_area = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited.add((r, c))
        area = 1

        while queue:
            pos_r, pos_c = queue.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dir_r, dir_c in directions:
                check_r = pos_r + dir_r
                check_c = pos_c + dir_c
                
                if (check_r in range(rows) and
                    check_c in range(cols) and
                    grid[check_r][check_c] == 1 and
                    (check_r, check_c) not in visited):
                    queue.append((check_r, check_c))
                    visited.add((check_r, check_c))
                    area += 1
            
        return area

    for r in range(rows):
        for c in range(cols):
            if (grid[r][c] == 1 and
                (r, c) not in visited):
                island_area = bfs(r, c)
                max_area = max(island_area, max_area)

    return max_area