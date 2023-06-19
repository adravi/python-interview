# https://leetcode.com/problems/contains-duplicate/description/

# Given an integer array nums, return true if any value appears at least twice in the array,
# return false if every element is distinct

# input: nums = [1,2,3,1]
# output: true

def containsDuplicate(nums):
    existing_nums = set()        # the key is having a set to look-up for already inspected nums

    for i in range(len(nums)):
        num = nums[i]

        if num in existing_nums:
            return True
        else:
            existing_nums.add(num)
    
    return False

# O(n) time
# O(n) space