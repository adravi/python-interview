# https://leetcode.com/problems/ransom-note/description/

# input: ransom_note = "aa", magazine = "ab"         // ransomeNode = n size  // magazine = m size
# output: false

# input: ransom_note = "aa", magazine = "aab"
# output: true

def canConstruct(ransom_note: str, magazine: str):
        map = {}
        for char in ransom_note:               # build a hashmap with the letters in 'ransom_note' and values as appearances
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        used_letters = 0
        for char in magazine:
            if char in map and map[char] > 0: # traverse 'magazine' and decrease the value of hashmap, if the same letter appears
                map[char] -= 1                  # ^ this would mean that a letter was 'used'
                counter += 1                  # keep track of used letters, to break the inspection as early as possible

            if used_letters == len(ransom_note):
                break

        for key in map:                       # if there is at least one letter that was not used, return False
            if map[key] > 0:
                return False

        return True                           # if all letters were used, return True

# O(n + m) time
# O(n) space