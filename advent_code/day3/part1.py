# https://adventofcode.com/2023/day/3

SYMBOLS = {"/", "+", "#", "$", "-", "&", "%", "=", "@", "*"}

def gears_ratios(grid: list[str]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0]) - 1
    nums = []

    for i in range(ROWS):
        num = ''
        adjacent_symbol = False

        for j in range(COLS):
            char = grid[i][j]

            if char.isdigit():
                if num:
                    num += char
                else:
                    num = char

                # left
                if j-1 in range(COLS) and grid[i][j-1] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # right
                if j+1 in range(COLS) and grid[i][j+1] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # up
                if i-1 in range(ROWS) and grid[i-1][j] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # down
                if i+1 in range(ROWS) and grid[i+1][j] in SYMBOLS:
                    adjacent_symbol += True
                    continue
          
                # diagonal up left
                if (j-1 in range(COLS) and i-1 in range(ROWS)) and grid[i-1][j-1] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # diagonal down left
                if (j-1 in range(COLS) and i+1 in range(ROWS)) and grid[i+1][j-1] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # diagonal up right
                if (j+1 in range(COLS) and i-1 in range(ROWS)) and grid[i-1][j+1] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # diagonal down right
                if (j+1 in range(COLS) and i+1 in range(ROWS)) and grid[i+1][j+1] in SYMBOLS:
                    adjacent_symbol += True
                    continue

                # EDGE CASE: reached end of line
                if j == COLS-1 and adjacent_symbol:
                    nums.append(int(num))
                    num = ''
                    adjacent_symbol = False

            elif not char.isdigit() and num:
                if adjacent_symbol:
                    nums.append(int(num))
                num = ''
                adjacent_symbol = False

    return sum(nums)


with open("./input.txt", "r", encoding="utf-8") as f:
    print(gears_ratios(f.readlines()))