
# https://www.youtube.com/watch?v=GcW4mgmgSbw&ab_channel=BytebyByte
# Every time we are looking at an overlapping sub-array, we can use the SlidingWindow to optime the solution

# We can contract the window on one side, and extend it on the other side, so we leverage the computing of elements
# in the middle. this wat, we dont start from scratch, unnecessarily computing again results that we already have

# Problem: Find the sum of each sub-array of length k and return an array with the corresponding sums
# input: array = [1, 2, 3, 4, 5, 6], k = 3
# output: [6, 9, 12, 15]

def fixed_sliding_window(array, k):
    # sum of the first subaray and add it to the results
    curr_subarray_sum = sum(array[:k])  # [:k] = first k elements in array
    result = [curr_subarray_sum]

    # to get each sub-sequent subarray, add the next value in the list and remove the first value
    for i in range(1, (len(array) - k + 1)):
        curr_subarray_sum = curr_subarray_sum - array[i - 1]     # substract element to the left
        curr_subarray_sum = curr_subarray_sum + array[i + k - 1] # add element to the right

        result.append(curr_subarray_sum)

    return result

# O(n) time
# O(1) space // the result array doesnt count. no aux-memory was used

print(fixed_sliding_window([1, 2, 3, 4, 5, 6], 3))
        
