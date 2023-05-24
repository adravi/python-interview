# https://www.algoexpert.io/questions/monotonic-array
# A monotonic array that array whose elements, from left to right, are entirely non-increasing or non-decreasing 
# input: [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# output: True

# AND boolean operations (Algebraic multiplied) :
    # True : True and True
    # False: True and False | False and True | False and False

# OR boolean operations (Algebraic sum):
    # True : True or False | False or True | True or True
    # False: False or False

def isMonotonic(array):
    monoUp = True
    monoDown = True

    # Make sure that i does not go beyond the penultimate index as [i + 1] will be used
    for i in range(len(array) - 1):
        # For monoUp or monoDown to stay True, both comparisons must always be True
        monoUp = monoUp and (array[i] <= array[i + 1])
        monoDown = monoDown and (array[i] >= array[i + 1])

    # At least one must be True, for the array to be monotonic
    return monoUp or monoDown

# O(n) T
# O(1) S

# ------------------------------------------------------------------------------------
