# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s):
    palindrome = ''
    maxLength = 0

    for i in range(len(s)):
        # odd length
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > maxLength:
                palindrome = s[left:right + 1]
                maxLength = (right - left + 1)
            left -= 1
            right += 1
            
        # even length
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > maxLength:
                palindrome = s[left:right + 1]
                maxLength = (right - left + 1)
            left -= 1
            right += 1
        
    return palindrome