# https://leetcode.com/problems/product-of-array-except-self/
# input:    [1, 2, 3, 4]
# outout:   [24, 12, 8, 6]

# Explanation: https://www.youtube.com/watch?v=bNvIQI2wAjk&ab_channel=NeetCode

def productExceptSelf(nums):
    result = len(nums)*[1]   # create an array to store the result and initialize it with 1
    pre = len(nums)*[1]      # create an array to store prefix products and initialize it with 1
    post= len(nums)*[1]      # create an array to store suffix products and initialize it with 1
    pref, postf = 1 , 1      # initialize prefix and suffix products to 1
    
    # calculate prefix products
    for i in range(len(nums)):
        pre[i]= pref       # store the prefix product of nums[0:i] in pre[i]
        pref *= nums[i]    # update the prefix product by multiplying with the current number
        
    # calculate suffix products
    for i in reversed(range(len(nums))):
        post[i]= postf      # store the suffix product of nums[i+1:n] in post[i]
        postf *=nums[i]     # update the suffix product by multiplying with the current number
    
    result[0]= post[0]       # set result[0] to the suffix product of the last element
    result[len(nums)-1] = pre[len(nums)-1]   # set result[n-1] to the prefix product of the first element
    
    # calculate product of prefix and suffix values
    for i in range (1,len(nums)-1):
        result[i]=pre[i]*post[i]   # compute the product of prefix and suffix values
    
    return result     # return the final result array

# O(n) Time | O(2n) -> O(n)
# O(n) Space
# ---------------------------------------------------------------------------------------------------------

# Solution using optimal space: No prefix and postfix arrays
def productExceptSelf(nums):
    result = len(nums)*[1]

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in reversed(range(len(nums))):
        result[i] *= postfix
        postfix *= nums[i]

    return result 

# O(n) Time | O(2n) -> O(n)
# O(1) Space