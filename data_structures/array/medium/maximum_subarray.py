# https://leetcode.com/problems/maximum-subarray/
# explanation: https://www.youtube.com/watch?v=5WZl3MMT0Eg&ab_channel=NeetCode

# input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# output: 6 // The subarray [4,-1,2,1] has the largest sum 6

# NOTE that we only want to return the LARGEST SUBARRAY SUM, not the actual SUBARRAY

def maxSubArray(nums):        # Technique is a sliding window that expands to the right, but reduces to the left
    maxSubarraySum = nums[0]
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0

        currSum += num
        maxSubarraySum = max(currSum, maxSubarraySum)
    
    return maxSubarraySum

# O(n) time
# O(1) space