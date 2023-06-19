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
    mono_up = True
    mono_down = True

    for i in range(len(array) - 1): # make sure that i does not go beyond the penultimate index as [i + 1] will be used
        # for mono_up or mono_down to stay True, both comparisons must always be True
        mono_up = mono_up and (array[i] <= array[i + 1])
        mono_down = mono_down and (array[i] >= array[i + 1])

    return mono_up or mono_down   # at least one must be True, for the array to be monotonic

# O(n) time
# O(1) space
