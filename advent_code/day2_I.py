# https://adventofcode.com/2023/day/2

RED, GREEN, BLUE = 12, 13, 14

input = [] # See inputs

def cubes_game(games):
    ids_sum = 0

    for id, game in enumerate(games):
        game_id = id + 1
        
        for cubeset in game:
            if 'r' in cubeset and cubeset['r'] > RED:
                break
            if 'g'in cubeset and cubeset['g'] > GREEN:
                break
            if 'b'in cubeset and cubeset['b'] > BLUE:
                break
        else:
            # All cubesets of Game are valid
            ids_sum += game_id
            continue
  
    return ids_sum

print(cubes_game(input))