# https://leetcode.com/problems/binary-search/
# array of nums is SORTED IN ASCENDING ORDER

# input: nums = [-1,0,3,5,9,12], target = 9
# output: 4

def search(nums, target):
    left = 0
    right = len(nums) - 1
    mid = 0

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] < target:      # target is greater, search on the right half
            left = mid + 1
        
        elif nums[mid] > target:    # target is smaller, search the left half
            right = mid - 1
        
        if nums[mid] == target:     # found!
            return mid

    return -1   # If we reach here, then the element was not present


# O(log(n)) Time
# O(1) Space

search([-1,0,3,5,9,12], 9)


     
