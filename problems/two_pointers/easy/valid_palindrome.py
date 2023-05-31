# https://leetcode.com/problems/valid-palindrome/
# input: 'A man, a plan, a canal: Panama'
#   After removing non-alphanumeric chars: 'amanaplanacanalpanama' // Is a palindrome!
# output: True

def isValidPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    
    leftPointer = 0
    rightPointer = len(s) - 1

    while leftPointer <= rightPointer:
        leftChar = s[leftPointer]
        rightChar = s[rightPointer]

        if leftChar.isalnum() and rightChar.isalnum():
            if leftChar.lower() != rightChar.lower():
                return False
            else:
                leftPointer += 1
                rightPointer -= 1

        elif not leftChar.isalnum():
            leftPointer += 1

        elif not rightChar.isalnum():
            rightPointer -= 1

    return True


# O(n) Time
# O(1) Space

isValidPalindrome("A man, a plan, a canal: Panama")
isValidPalindrome('"race a car"')
isValidPalindrome(' ')
