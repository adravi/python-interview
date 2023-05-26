# https://leetcode.com/problems/contains-duplicate/description/

# Given an integer array nums, return true if any value appears at least twice in the array,
# return false if every element is distinct

# Input: nums = [1,2,3,1]
# Output: true

def containsDuplicate(nums) -> bool:
    existingNums = set()

    for i in range(len(nums)):
        num = nums[i]

        if num in existingNums:
            return True
        else:
            existingNums.add(num)
    
    return False

# O(n) Time
# O(n) Space