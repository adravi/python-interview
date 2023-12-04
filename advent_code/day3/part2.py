# https://adventofcode.com/2023/day/3#part2

def gears_ratios(grid: list[str]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0]) - 1
    nums = []
    star_map = {}
    res = 0

    for i in range(ROWS):
        num = ''
        adjacent_star = False
        coordinate = ()

        for j in range(COLS):
            char = grid[i][j]

            if char.isdigit():
                if num:
                    num += char
                else:
                    num = char

                # left
                if j-1 in range(COLS) and grid[i][j-1] == '*':
                    adjacent_star = True
                    coordinate = (i, j-1)

                # right
                if j+1 in range(COLS) and grid[i][j+1] == '*':
                    adjacent_star = True
                    coordinate = (i, j+1)
                    
                # up
                if i-1 in range(ROWS) and grid[i-1][j] == '*':
                    adjacent_star = True
                    coordinate = (i-1, j)

                # down
                if i+1 in range(ROWS) and grid[i+1][j] == '*':
                    adjacent_star = True
                    coordinate = (i+1, j)
          
                # diagonal up left
                if (j-1 in range(COLS) and i-1 in range(ROWS)) and grid[i-1][j-1] == '*':
                    adjacent_star = True
                    coordinate = (i-1, j-1)
                    
                # diagonal down left
                if (j-1 in range(COLS) and i+1 in range(ROWS)) and grid[i+1][j-1] == '*':
                    adjacent_star = True
                    coordinate = (i+1, j-1)
                    
                # diagonal up right
                if (j+1 in range(COLS) and i-1 in range(ROWS)) and grid[i-1][j+1] == '*':
                    adjacent_star = True
                    coordinate = (i-1, j+1)

                # diagonal down right
                if (j+1 in range(COLS) and i+1 in range(ROWS)) and grid[i+1][j+1] == '*':
                    adjacent_star = True
                    coordinate = (i+1, j+1)

                # EDGE CASE: reached end of line
                if j == COLS-1 and adjacent_star:
                    number = int(num)
                    nums.append(number)
                    
                    if coordinate in star_map:
                        star_map[coordinate].append(number)
                    else:
                        star_map[coordinate] = [number]
                    
                    num = ''
                    adjacent_star = False

            elif not char.isdigit() and num:
                number = int(num)

                if adjacent_star:
                    nums.append(number)
                    if coordinate in star_map:
                        star_map[coordinate].append(number)
                    else:
                        star_map[coordinate] = [number]

                num = ''
                adjacent_star = False

    # lookup for start coordinates that have exactly 2 registered adjacent numbers
    for coordinate, numbers in star_map.items():
        if len(numbers) == 2:
            res += numbers[0] * numbers[1]
    
    return res


with open("./input.txt", "r", encoding="utf-8") as f:
    print(gears_ratios(f.readlines()))