# https://www.algoexpert.io/questions/two-number-sum 
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Create a hash-set using the array as input and referencing each element as 'num'
def two_number_rsum(array, targetSum):
    nums = set(num for num in array)
    
    for num in array:
        rec = targetSum - num

        if (rec in nums and
            rec != num):
            # Found the pair!
            return [num, rec]
    
    return []

# O(n) time
# O(n) space