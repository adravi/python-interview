# https://leetcode.com/problems/koko-eating-bananas/

import math

def minEatingSpeed(piles, h):
    piles.sort()    # O(n(log(n)))
    
    k = piles[0]
    while k <= piles[-1]:
        hoursConsumed = 0
        for pile in piles:
            hoursCoeficient = math.ceil(pile / k)
            hoursConsumed += hoursCoeficient

        if hoursConsumed <= h:
            break
        else:
            k += 1

    return k
        
minEatingSpeed([3, 6, 7, 11], 8)