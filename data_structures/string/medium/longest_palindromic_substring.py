# https://leetcode.com/problems/longest-palindromic-substring/

# input: s = "babad"
# output: "bab" / "aba" is also a valid answer

# input: s = "cbbd"
# output: "bb"

def longestPalindrome(s): # Trick is to start from the 'center' and expand to left and right, compasing chars at the extremes
    palindrome = ''
    maxLength = 0

    for i in range(len(s)):
        # odd length
        left, right = i, i                                          # for 'aba' odd palindromes, start at the same index i
        while left >= 0 and right < len(s) and s[left] == s[right]: # keep left and right pointrs in-bound and see if they match
            if (right - left + 1) > maxLength:                      # calculate length
                palindrome = s[left:right + 1]                      # update the palindrome if its length is larger
                maxLength = (right - left + 1)                      # don't forget to update maxLength!
            left -= 1  # regardless, expand palindrome to the left
            right += 1 # regardless, expand palindrome to the right
            
        # even length
        left, right = i, i+1                                        # for 'aba' odd palindromes, start at index i and i+1
        while left >= 0 and right < len(s) and s[left] == s[right]: # keep left and right pointrs in-bound and see if they match
            if (right - left + 1) > maxLength:                      # calculate length
                palindrome = s[left:right + 1]                      # update the palindrome if its length is larger
                maxLength = (right - left + 1)                      # don't forget to update maxLength!
            left -= 1  # regardless, expand palindrome to the left
            right += 1 # regardless, expand palindrome to the right                                             

    return palindrome