# https://leetcode.com/problems/ransom-note/description/

# input: ransomNote = "aa", magazine = "ab"         // ransomeNode = n size  // magazine = m size
# output: false

# input: ransomNote = "aa", magazine = "aab"
# output: true

def canConstruct(ransomNote: str, magazine: str):
        map = {}
        for char in ransomNote:               # build a hashmap with the letters in 'ransomNote' and values as appearances
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        usedLetters = 0
        for char in magazine:
            if char in map and map[char] > 0: # traverse 'magazine' and decrease the value of hashmap, if the same letter appears
                map[char] -= 1                  # ^ this would mean that a letter was 'used'
                counter += 1                  # keep track of used letters, to break the inspection as early as possible

            if usedLetters == len(ransomNote):
                break

        for key in map:                       # if there is at least one letter that was not used, return False
            if map[key] > 0:
                return False

        return True                           # if all letters were used, return True

# O(n + m) time
# O(n) space