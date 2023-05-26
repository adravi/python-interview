# https://leetcode.com/problems/merge-sorted-array/
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1
# Do not return anything, modify nums1 in-place instead.

def merge(self, nums1, m, nums2, n):
    # Pointer for nums1, from right to left, on the m portion
    i = m - 1

    # Pointer for nums2, from right to left
    j = n - 1

    # Pointer for inserting the numbers in the sorted array
    k = m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

# O(m+n) Time
# We are iterating through both arrays once

# O(1) Space
# We are not using any extra space
# ------------------------------------------------------------------------------------

# We can start with two pointers i and j, initialized to m-1 and n-1, respectively

# We will also have another pointer k initialized to m+n-1, 
# which will be used to keep track of the position in nums1 where we will be placing the larger element

# Then we can start iterating from the end of the arrays i and j, and compare the elements at these positions
# We will place the larger element in nums1 at position k, and decrement the corresponding pointer i or j accordingly
# We will continue doing this until we have iterated through all the elements in nums2
# If there are still elements left in nums1, we don't need to do anything because they are already in their correct place