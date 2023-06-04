# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# input: s = "abcabcbb"
# output: 3 // 'abc'

# input: s = "bbbbb"
# output: 1

# SlidingWindow: Reduce windows from the left, extend it to the right. Leave center untouched to not start from scratch
def lengthOfLongestSubstring(s):
    charSet = set()
    maxLen = 0
    left = 0

    for right in range(len(s)):
        while s[right] in charSet:  # Check if the inspected char already exsts in substring
            charSet.remove(s[left]) # Remove chars until the repeated char is gone from the set
            left += 1
        
        charSet.add(s[right])       # Add the new char to the set
        len = right - left + 1      # Calculate the current substring length by substracting indices (remember: base 0)
        maxLen = max(maxLen, len)   # Update the maxLength

    return maxLen

# O(n) time
# O(n) space