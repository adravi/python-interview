# https://adventofcode.com/2023/day/2

RED, GREEN, BLUE = 12, 13, 14

input = [] # see inputs

def cubes_game(games):
    pow_sum = 0

    for game_id, game in enumerate(games):
        max_r, max_g, max_b, power = float('-inf'), float('-inf'), float('- inf'), 0

        for cubeset in game:
            if 'r' in cubeset:
                max_r = max(max_r, cubeset['r'])
            if 'g'in cubeset:
                max_g = max(max_g, cubeset['g'])
            if 'b'in cubeset:
                max_b = max(max_b, cubeset['b'])

        power = max_r * max_g * max_b
        print('Game', game_id + 1, '| r:', max_r, 'g:', max_g, 'b:', max_b, ' | POW:', power)
        pow_sum += power
        print('sum:', pow_sum)

    return pow_sum

print(cubes_game(input))