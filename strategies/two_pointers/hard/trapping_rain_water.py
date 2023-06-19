# https://leetcode.com/problems/trapping-rain-water/

# input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# output: 6
# The above elevation map (black section) is represented by array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# In this case, 6 units of rain water (blue section) are being trapped // see input1

# input: height = [4, 2, 0, 3, 2, 5]
# output: 9 // see input2

def water_trap(height):
    if len(height) == 0 or len(height) == 1:
        return 0

    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[r]
    res = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            res += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            res += right_max - height[right]
        
    return res


print(water_trap([0,1,0,2,1,0,1,3,2,1,2,1]))
