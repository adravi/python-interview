# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Input: numbers = [2,7,11,15], target = 9
# output: [1,2] // The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]

def twoSum(numbers, target): # strategy is TwoPointers, left and right as far most as possible. TRICK: ARRAY IS SORTED
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum1 = numbers[left] + numbers[right] # calculate sum and update pointers by comparing it to the target

        if sum1 < target:   # if the target is larger, move left ptr to the left in-wards, increasing the sum
            left += 1        
        elif sum1 > target: # if the target is smaller, move right ptr to the right in-wards, decreasing the sum
            right -= 1
        else:
            # target == sum1
            return [left + 1, right + 1] # the problem requires returning an array[leftIdx + 1, rightIdx + 1 ] FOR NO REASON

    return [-1, -1]


# O(n) time
# O(1) space