# https://www.algoexpert.io/questions/non-constructible-change
# [5, 7, 1, 1, 2, 3, 22]

def nonConstructibleChange(coins):
    # basic cases
    if len(coins) == 0:
        return 1
    elif len(coins) == 1 and coins[0] != 1:
        return 1

    # sort array ASC: O(n log(n)) T -> It uses quicksort
    coins.sort()

    curr_change = 0

    for coin in coins:
        # inspect the current coin. Is it greater than curr_change + 1 ?
        if coin > curr_change + 1:
            # If so, we cannot create the value of curr_change + 1
            return curr_change + 1
        
        # otherwise, add-up the value of the inspected coin
        curr_change += coin

    return curr_change + 1

# O((n log(n)) + n) -> O(n log(n)) time
# O(1) space -> Because we sorted the array in-place
