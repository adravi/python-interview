# https://www.algoexpert.io/questions/two-number-sum 
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Solution
def twoNumberSum(array, targetSum):
    # Empty HasMap
    map = {}
    
    for i in range(len(array)):
        # Build the reciprocate map
        rec = targetSum - array[i]
        map[rec] = array[i]
    
    for i in range(len(array)):
        num = array[i]
        # Make sure that the pair is given by diff nums in array
        if (num in map) and (num != map[num]):
            # Found the pair!
            return [num, map[num]]

    return []

# O(n) S
# O(2n) -> O(n) T
# ---------------------------------------------------------------

# Solution improved
def twoNumberSum(array, targetSum):
    # Create a HashSet using the array as input and referencing each element as 'num'
    nums = set(num for num in array)
    
    for num in array:
        rec = targetSum - num

        if (rec in nums) and (rec != num):
            # Found the pair!
            return [num, rec]
    
    return []

# O(n) S
# O(n) T