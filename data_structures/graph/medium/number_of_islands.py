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

def num_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited  = set()
    islands = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited.add((r, c))

        while queue:
            pos_r, pos_c = queue.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dir_r, dir_c in directions:
                check_r = pos_r + dir_r
                check_c = pos_c + dir_c
                
                if (check_r in range(rows) and
                    check_c in range(cols) and
                    grid[check_r][check_c] == '1' and
                    (check_r, check_c) not in visited):

                    queue.append((check_r, check_c))
                    visited.add((check_r, check_c))


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands

# explanation: https://www.youtube.com/watch?v=pV2kpPD66nE&ab_channel=NeetCode