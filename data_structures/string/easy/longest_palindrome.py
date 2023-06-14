# https://leetcode.com/problems/longest-palindrome/
# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.

# input: s = "abccccdd"
# output: 7 / one longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(self, s: str) -> int: # palindromes are formed by matching-pairs of chars + 1 single (goes in the middle)
    singles = set() # set to store the single found char
    length = 0

    for char in s:
        if char in singles:      # if we find a matching char, we can remove it (to start again)
            singles.remove(char)
            length += 2          # and increase the palindrome length by 2 (since we technically accounted for a pair)
        else:
            singles.add(char)    # we just found a single
    
    if len(singles) > 0:         # in the end, if we have found any single, we can add it up to the length of palindrome
        length += 1
    
    return length

# O(n) time
# O(1) space