# https://leetcode.com/problems/number-of-islands/
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
You may assume all four edges of the grid are all surrounded by water

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

# strategy: for each ceil containing '1', expand the exploration of the neighbor nodes as a graph traversal (BFS in this case)
# although this problem is about a grid, it can be solved as A GRAPH TRAVERSAL
def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0]) # have the width and heigth dimensions as variables from the beginning
    visited  = set()                     # as any other implementation of BFS, have a set() to not visit nodes twice
    islands = 0

    def bfs(r, c):                       # Breadth First Search implementation
        queue = deque()                  # natural use of a 'queue'
        queue.append((r, c))
        visited.add((r, c))              # set() to not visit nodes more than once

        while queue:
            pos_r, pos_c = queue.popleft()                  # dequeue the most-left value from the queue
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # these are the 4 dirs of ceils to check: right, left, above, under
            
            for dir_r, dir_c in directions:             # apply one new direction at a time, to check the 4 ceils that
                check_r = pos_r + dir_r                 # can potentially contain a neighbour piece of land
                check_c = pos_c + dir_c                 # left, right, above, under
                
                if (check_r in range(rows) and          # the ceil to check, must be still within the boundaries of the grid
                    check_c in range(cols) and          # the ceil to check, must be still within the boundaries of the grid
                    grid[check_r][check_c] == '1' and   # check if it is, indeed, a piece of land
                    (check_r, check_c) not in visited): # IMPORTANT! make sure that the ceil hasn't been visited before

                    queue.append((check_r, check_c))    # if so, add it to the queue so the (node) can be explored as well
                    visited.add((check_r, check_c))     # make sure to mark it as visited, so it's not counted twice as part of some island


    for r in range(rows):               # classic nested for-loop to explore the grid (matrix, 2D array)
        for c in range(cols):
            if (grid[r][c] == '1' and   # if the ceil represents a piece of land, and this node hasn't been explored...
                (r, c) not in visited):
                bfs(r, c)               # keep expanding this piece of land, by performing BFS on this ceil (node)
                islands += 1            # in the end, this piece of land will represent a new island

    return islands

# O(n*m) time  // n and m being the dimension sizes of the grid
# O(n*m) space // the queue and set() are aux memory

# explanation: https://www.youtube.com/watch?v=pV2kpPD66nE&ab_channel=NeetCode