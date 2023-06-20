# https://leetcode.com/problems/car-fleet/
# input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# output: 3

"""
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12
The car starting at 0 does not catch up to any other car, so it is a fleet by itself
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6.
The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3
"""

def carFleet(target, positions, speeds):                # First, have a list with each element being: [position, speed]
    pairs = [[p, s] for p, s in zip(positions, speeds)] # zip(): joins two lists together
                                                        # https://www.w3schools.com/python/ref_func_zip.asp
    stack = []
    
                                                   # traverse the array from right to left, as slow cars absorb faster cars
    for pos, speed in sorted(pairs)[::-1]:         # sorted(list)[::1] : Reverse Sorted Order
        miles_to_target = (target - pos) / speed   # calculate the miles still missing to meet the target (decimal division)
        stack.append(miles_to_target)              # push it to the stack, representing one car
        
        if len(stack) >= 2 and stack[-1] <= stack[-2]: # if there is, at least, 2 cars to compare 
            stack.pop()                                # if they collide you can take out one of them
                                                       # since they merged into a 'fleet'
    return len(stack)                                  # simply return the size of stack

# O(n) time
# O(n) space

# see car_fleet_explanation1 and car_fleet_explanation2
# https://www.youtube.com/watch?v=Pr6T-3yB9RM&t=594s&ab_channel=NeetCode