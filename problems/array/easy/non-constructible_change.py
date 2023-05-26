# https://www.algoexpert.io/questions/non-constructible-change
# [5, 7, 1, 1, 2, 3, 22]

def nonConstructibleChange(coins):
    # Basic cases
    if len(coins) == 0:
        return 1
    elif len(coins) == 1 and coins[0] != 1:
        return 1

    # Sort array ASC: O(n log(n)) T -> It uses quicksort
    coins.sort()

    currentChange = 0

    for coin in coins:
        # Inspect the current coin. Is it greater than currentChange + 1 ?
        if coin > currentChange + 1:
            # If so, we cannot create the value of currentChange + 1
            return currentChange + 1
        
        # Otherwise, add-up the value of the inspected coin
        currentChange += coin

    return currentChange + 1

# O((n log(n)) + n) -> O(n log(n)) Time
# O(1) Space -> Because we sorted the array in-place
