# https://leetcode.com/problems/container-with-most-water/
# input: height = [1,8,6,2,5,4,8,3,7]
# output: 49 / 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7] (see input image)
# In this case, the max area of water the container can contain is 49

# strategy is to start with 2 pointers as far away as possible, trying to maximize the rectangle area
# [1, 8, 6, 2, 5, 4, 8, 3, 7]
#  L ->                <-  R
def maxArea(height): 
    left = 0
    right = len(height) - 1
    maxArea = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left) # area is given by: min(arr[left], arr[right]) * (right - left)
        maxArea = max(area, maxArea) # update max area
           
                                            # now try to find potentially larger values that can maximize the area
        if height[left] <= height[right]:   # if the value at arr[left] is smaller than arr[right], move left by 1 inwards
            left += 1
        else: 
            # height[left] < height[right]  # if the value at arr[right] is smaller than arr[small], move right by 1 inwards
            right -= 1
    
    return maxArea

# O(n) time
# O(1) space