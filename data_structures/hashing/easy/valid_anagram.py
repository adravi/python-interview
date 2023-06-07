# https://leetcode.com/problems/valid-anagram/

def isAnagram(s, t):
        if len(s) != len(t):
            return False

        letterMap = {}
        for i in range(len(t)):
            if t[i] not in letterMap:
                 letterMap[t[i]] = 1
            else:
                 letterMap[t[i]] += 1

        for i in range(len(s)):
            if s[i] not in letterMap or letterMap[s[i]] < 1:
                return False
            else:
                letterMap[s[i]] -= 1
        
        return True

# O(n) Time
# O(n) Space

print(isAnagram("anagram", "nagaram"))