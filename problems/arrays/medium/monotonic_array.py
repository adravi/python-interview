# https://www.algoexpert.io/questions/monotonic-array
# A monotonic array that array whose elements, from left to right, are entirely non-increasing or non-decreasing 
# input: [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

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
def isMonotonic(array):
    i = 0
    j = 1
    monoUp = None

    # Look for a pair of different nums whose substraction indicates the mono-trend (up/down)
    while j < len(array) and monoUp == None:
        if array[i] != array[j]:
            monoUp = True if (array[j] - array[i] > 0) else False

        i,j = i+1, j+1

    # MonoUp either being True or False must be maintained across the whole array
    while j < len(array):
        diff = array[j] - array[i]
        if diff > 0 and not monoUp:
            # Monotonic downwards broken!
            return False
        elif diff < 0 and monoUp:
            # Monotonic upwards broken!
            return False

        i,j = i+1, j+1

    # If the whole array has been traversed without breaking Mono, then it is monotonic, indeed     
    return True
