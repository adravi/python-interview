# https://leetcode.com/problems/largest-rectangle-in-histogram/

# input: heights = [2,1,5,6,2,3]
# output: 10

# The above is a histogram where width of each bar is 1 (see input image)
# The largest rectangle is shown in the red area, which has an area = 10 units


# strategy is to pop() out the heights, from which we cannot keep extending the 'rectangle'
def largest_rectangle_area(heights):
    max_area = 0
    stack = [] # pair: (index, height)

    for curr_idx, curr_height in enumerate(heights):
        rect_start_idx = curr_idx
        
        while stack and stack[-1][1] > curr_height: # if the prev height is higher than the current, we cant extend rect
            (start_idx_at_this_height, height) = stack.pop()
            max_area = max(max_area, height * (curr_idx - start_idx_at_this_height))
            rect_start_idx = start_idx_at_this_height

        stack.append((rect_start_idx, curr_height)) # either append the current index, or the index where the rect started

    for start_idx_at_this_height, height in stack:  # in the end, there are potential rectangles that we need to check
        max_area = max(max_area, height * (len(heights) - start_idx_at_this_height))
     
    return max_area

# O(n) time
# O(n) space // the stack is extra aux mem


# explanation: https://www.youtube.com/watch?v=zx5Sw9130L0&ab_channel=NeetCode


# print(largest_rectangle_area([2,1,5,6,2,3]))
# print(largest_rectangle_area([1,2,2]))
# print(largest_rectangle_area([1,2,3,4,5]))