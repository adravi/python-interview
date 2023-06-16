# https://leetcode.com/problems/maximum-subarray/
# explanation: https://www.youtube.com/watch?v=5WZl3MMT0Eg&ab_channel=NeetCode

# input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# output: 6 // The subarray [4,-1,2,1] has the largest sum 6

# NOTE that we only want to return the LARGEST SUBARRAY SUM, not the actual SUBARRAY

def maxSubArray(nums):        # technique is a sliding window that expands to the right, but reduces to the left
                              # we will get rid of any 'prefix' (set of numbers) that produce a negative sum
    maxSubarraySum = nums[0]  
    currSum = 0

    for num in nums:
        if currSum < 0:       # if the current sum ever becomes negative, reset it to 0. We dont need negative 'prefixes'
            currSum = 0

        currSum += num        # simply add the next number
        maxSubarraySum = max(currSum, maxSubarraySum)   # update the largest subarray sum
    
    return maxSubarraySum

# O(n) time
# O(1) space