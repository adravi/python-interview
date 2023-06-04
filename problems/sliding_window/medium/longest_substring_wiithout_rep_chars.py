# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# input: s = "abcabcbb"
# output: 3 // 'abc'

# input: s = "bbbbb"
# output: 1

def lengthOfLongestSubstring(s):
    charSet = set()
    maxLength = 0
    left = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        
        charSet.add(s[right])
        maxLength = max(maxLength, (right - left + 1))

    return maxLength