# https://leetcode.com/problems/koko-eating-bananas/
# Return the minimum integer k (speed) such that she can eat all the bananas within h hours
# input: piles = [3,6,7,11], h = 8
# output: 4

# hint: They will give you a piles array of size n, where n is bigger or equal than hours (we can count on it)
#       This means that, at least, you will have 1 hours to consume each pile

# brute-force approach: from 1 to maxValue in piles, try each number as potential k (speed),
# c                     alculting the total hours consumed and compare it with h. Look for the minimum

# binary-search: we can reduce the complexity by applying BS to the series 1-maxValue, looking in the other half
#                of the array as we try-out a potential k (speed) and compare the consumedHours to hours

import math
def minEatingSpeed(piles, h):
    k = float('inf')

    left = 1
    right = max(piles)
    while left <= right:                # implement BS to a sequential series 1-maxValue (no arrray necessary)
        mid = (left + right) // 2

        hoursConsumed = 0
        for pile in piles:
            speedCoeficient = math.ceil(pile / mid) # divide (bananasInPile / potentialK). it's integer TOP division!
            hoursConsumed += speedCoeficient        # accumulate the value of hours consumed so far with potential k

        if hoursConsumed <= h:
            k = min(k, mid)     # you have found a valid k, but keep looking for a smaller one on the left half of series
            right = mid - 1

        else: # hoursConsumed > h
            left = mid + 1      # k (speed) was too low, look on the right half for a larger k

    return k

# O(log(maxPile) * len(piles)) time
# O(1) space

minEatingSpeed([3, 6, 7, 11], 8)