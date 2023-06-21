# https://leetcode.com/problems/largest-rectangle-in-histogram/

def largest_rectangle_area(heights):
    stack = [] # pair: (index, height)
    max_area = 0

    for curr_idx, curr_height in enumerate(heights):
        rect_start_idx = curr_idx
        
        while stack and stack[-1][1] > curr_height:
            (start_idx_at_this_height, height) = stack.pop()
            max_area = max(max_area, height * (curr_idx - start_idx_at_this_height))
            rect_start_idx = start_idx_at_this_height

        stack.append(rect_start_idx, curr_height)

    for start_idx_at_this_height, height in stack:
        max_area = max(max_area, height * (len(heights) - start_idx_at_this_height))
     
    return max_area


# print(largest_rectangle_area([2,1,5,6,2,3]))
# print(largest_rectangle_area([1,2,2]))
print(largest_rectangle_area([1,2,3,4,5]))