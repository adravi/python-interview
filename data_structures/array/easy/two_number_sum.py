# https://www.algoexpert.io/questions/two-number-sum 
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

def twoNumberSum(array, targetSum):  # Create a hash-set using the array as input and referencing each element as 'num'
    nums = set(num for num in array)
    
    for num in array:
        rec = targetSum - num

        if (rec in nums) and (rec != num):
            # Found the pair!
            return [num, rec]
    
    return []

# O(n) time
# O(n) space