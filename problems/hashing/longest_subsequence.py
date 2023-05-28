# https://leetcode.com/problems/longest-consecutive-sequence/
# Explanation: https://www.youtube.com/watch?v=P6RZZMu_maU&ab_channel=NeetCode

# input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# output: 9 // 0 1 2 3 4 5 6 7 8

# We have to find all sequences and compare their length
# The trick is to found the starting number of each potential sequence by checking if its prevNum exists or not
def longestSubsequence(nums):
    # Create a set out of the list
    numSet = set(nums)
    longestLength = 0

    # We will find the nums that be the start of each potential sequences
    for num in nums:
        if (num - 1) not in numSet:     # We look-up if the prevNum in a potential sequence exists in the set
            sequenceLength = 0          # This num is the start of a potential sequence, because the prevNum isn't in the set!
            while num + sequenceLength in numSet:   # We keep exploring if the nextNum exists, exteding this sequence
                sequenceLength += 1                 # sequenceLength also help us to keep traversing the potential sequence

            longestLength = max(sequenceLength, longestLength)  # Update the length of found sequence to the longest one
    
    return longestLength


